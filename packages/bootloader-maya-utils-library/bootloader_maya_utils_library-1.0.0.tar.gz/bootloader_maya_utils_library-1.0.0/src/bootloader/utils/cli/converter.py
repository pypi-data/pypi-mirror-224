#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
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

import argparse
import os
from os import PathLike
from pathlib import Path

from majormode.perseus.constant.logging import LOGGING_LEVEL_LITERAL_STRINGS
from majormode.perseus.constant.logging import LoggingLevelLiteral
from majormode.perseus.utils import env
from majormode.perseus.utils.logging import DEFAULT_LOGGING_FORMATTER
from majormode.perseus.utils.logging import cast_string_to_logging_level
from majormode.perseus.utils.logging import set_up_logger

from bootloader.utils.maya import converter


DEFAULT_MAYA_BINARY_FILE_PATH_NAME= Path('/Applications/Autodesk/maya2024/Maya.app/Contents/bin/maya')


def cast_string_to_path(path: str) -> PathLike:
    return Path(os.path.expanduser(path))


def parse_arguments() -> argparse.Namespace:
    """
    Convert argument strings to objects and assign them as attributes of
    the namespace.


    :return: An instance `Namespace` corresponding to the populated
        namespace.
    """
    parser = argparse.ArgumentParser(description="Maya utilities")

    parser.add_argument(
        '--animated-gif-image-quality',
        dest='animated_gif_image_quality',
        metavar='QUALITY',
        required=False,
        default=75,
        type=int,
        help="specify the compression quality factor to use for the movie file. "
             "Value should be in the 0-100 range."
    )

    parser.add_argument(
        '--animated-gif-image-size',
        dest='animated_gif_image_size',
        metavar='GEOMETRY',
        required=False,
        default="256x256",
        type=str,
        help="specify the width and height of the animated GIF image."
    )

    parser.add_argument(
        '--logging-level',
        dest='logging_level',
        metavar='LEVEL',
        required=False,
        default=str(LoggingLevelLiteral.info),
        type=cast_string_to_logging_level,
        help=f"specify the logging level ({', '.join(LOGGING_LEVEL_LITERAL_STRINGS)})"
    )

    parser.add_argument(
        '--maya-animation-file-path-name',
        dest='maya_animation_file_path_name',
        metavar='FILE',
        required=True,
        type=cast_string_to_path,
        help="specify the path and name of the Maya animation file to convert"
    )

    parser.add_argument(
        '--maya-binary-file-path-name',
        dest='maya_binary_file_path_name',
        metavar='FILE',
        required=False,
        default=None,
        type=cast_string_to_path,
        help="specify Maya binary file's path and name"
    )

    parser.add_argument(
        '--maya-project-path',
        dest='maya_project_path',
        metavar='PATH',
        required=True,
        default=None,
        type=cast_string_to_path,
        help="specify the path of the Maya project's folder"
    )

    return parser.parse_args()


def run():
    arguments = parse_arguments()

    set_up_logger(
        logging_formatter=DEFAULT_LOGGING_FORMATTER,
        logging_level=arguments.logging_level
    )

    converter.generate_animated_gif_file(
        arguments.maya_project_path,
        arguments.maya_animation_file_path_name,
        maya_binary_file_path_name=arguments.maya_binary_file_path_name
    )

run()