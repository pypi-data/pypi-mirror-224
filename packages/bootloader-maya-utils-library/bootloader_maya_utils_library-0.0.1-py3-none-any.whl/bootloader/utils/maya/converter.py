# Copyright (C) 2023 Bootloader.  All rights reserved.
#
# This software is the confidential and proprietary information of
# Bootloader or one of its subsidiaries.  You shall not disclose this
# confidential information and shall use it only in accordance with the
# terms of the license agreement or other applicable agreement you
# entered into with Bootloader.
#
# BOOTLOADER MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE
# SUITABILITY OF THE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR
# A PARTICULAR PURPOSE, OR NON-INFRINGEMENT.  BOOTLOADER SHALL NOT BE
# LIABLE FOR ANY LOSSES OR DAMAGES SUFFERED BY LICENSEE AS A RESULT OF
# USING, MODIFYING OR DISTRIBUTING THIS SOFTWARE OR ITS DERIVATIVES.

import logging
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
from os import PathLike
from pathlib import Path

from majormode.perseus.utils import env
from pygifsicle import gifsicle

from bootloader.utils.maya.playblast import PlayblastCommandBuilder

# Default path where Autodesk applications are typically installed on a
# macOS machine.
DEFAULT_MACOS_AUTODESK_PATH = '/Applications/Autodesk'


def find_maya_binary_file_path_name() -> PathLike:
    """
    Return Maya's path and binary file name.

    :return:

:raise Exception: If the operating system of the machine on which this
    script is running is not supported, or if Maya application has not
    been found.
    """
    if sys.platform != 'darwin':
        raise Exception(f"Unsupported operating system {sys.platform}")

    if not os.path.exists(DEFAULT_MACOS_AUTODESK_PATH):
        raise Exception("No Autodesk applications seem to be installed on this computer")

    for root, dirs, file_names in os.walk(DEFAULT_MACOS_AUTODESK_PATH):
        for file_name in file_names:
            if file_name == 'maya':
                maya_binary_file_path_name = os.path.join(root, file_name)
                return Path(maya_binary_file_path_name)


def generate_animated_gif_file(
        maya_project_path: PathLike,
        maya_animation_file_path_name: PathLike,
        animated_gif_image_frame_padding: int = 4,
        animated_gif_image_quality: int = 70,
        animated_gif_image_size: (int, int) or None= None,
        animated_gif_file_path_name: PathLike = None,
        maya_binary_file_path_name: PathLike or None = None) -> PathLike:
    if not maya_binary_file_path_name:
        maya_binary_file_path_name = find_maya_binary_file_path_name()
        logging.debug(f"Using Maya {maya_binary_file_path_name}")

    # Create a temporary folder where the GIF files will be generated in.
    temporary_path = tempfile.mkdtemp()
    temporary_files_path_name_prefix = os.path.join(temporary_path, 'maya-animated-gif')

    # Build the Playblast MEL command to convert the Maya file to a series
    # of GIF files.
    playblast_command_builder = PlayblastCommandBuilder(
        temporary_files_path_name_prefix,
        frame_padding=animated_gif_image_frame_padding,
        image_size=animated_gif_image_size,
        quality=animated_gif_image_quality
    )

    # Generate the Shell command line with arguments to run Maya and execute
    # the MEL command.
    command_line_arguments = shlex.split(f'''
        {maya_binary_file_path_name} \
        -batch \
        -file "{maya_animation_file_path_name}" \
        -command '{playblast_command_builder.build()}'
    ''')

    # Set the Maya environment variable to specify the path of the Maya
    # project.  This is required to let Maya find all the assets that the
    # Maya animation file depends on.
    env.setenv('MAYA_PROJECT', maya_project_path)

    # Execute the Shell command and redirect stdout to the standard output.
    completed_process = subprocess.run(
        command_line_arguments,
        stdout=sys.stdout
    )

    if completed_process.returncode != 0:
        raise Exception(f"The Shell command has failed: {command_line_arguments}")

    # Combine all the GIF files into an animated GIF file.
    gif_file_names = sorted([
        file.absolute()
        for file in list(Path(temporary_path).iterdir())
        if file.is_file() and file.suffix == '.gif'
    ])

    if not animated_gif_file_path_name:
        animated_gif_file_path_name = Path(maya_animation_file_path_name).with_suffix('.gif')

    gifsicle(
        destination=str(animated_gif_file_path_name),
        sources=gif_file_names,
        colors=256,
        optimize=True,
        # Fix slow frame rate issue. Values 0 and 1 (hundredths of a second)
        # result in slow frame rate, while the frame rate was supposed to be
        # "no delay", respectively 1/100 s.  The value 2 provides the expecting
        # frame rate.
        #
        # References:
        # - https://superuser.com/questions/569924/why-is-the-gif-i-created-so-slow
        # - https://www.deviantart.com/humpy77/journal/Frame-Delay-Times-for-Animated-GIFs-214150546
        options=['--delay', '2']  #
    )

    # Delete the temporary folder where the GIF files have been generated
    # into.
    shutil.rmtree(temporary_path)

    return animated_gif_file_path_name
