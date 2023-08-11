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

from os import PathLike


class PlayblastCommandBuilder:
    """
    Builder of Maya Embedded Language [Playblast](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Tech-Docs/Commands/playblast.html)
    command.
    """
    DEFAULT_COMPRESSION = 'gif'
    DEFAULT_FRAME_PADDING = 4
    DEFAULT_IMAGE_SIZE = (256, 256)
    DEFAULT_OUTPUT_FORMAT = 'image'
    DEFAULT_QUALITY = 75
    DEFAULT_VIEW_PERCENT = 100

    def __init__(
            self,
            file_path_name: str or PathLike,
            clear_cache: bool = True,
            compression: str = None,
            frame_padding: int = None,
            image_size: tuple[int, int] = None,
            launch_viewer: bool = True,
            output_format: str = None,
            quality: int = None,
            sequence_time: int = 0,
            show_ornaments: bool = True,
            view_percent: int = None):
        """
        Build a new Playblast command.


        :param file_path_name: The path and name of the file to use for the
            output of this playblast.

        :param clear_cache: When ``True``, all previous temporary playblast
            files will be deleted before the new playblast files are created
            and the remaining temporary playblast files will be deleted when
            the application quits.  Any playblast files that were explicitly
            given a name by the user will not be deleted.

        :param compression: Specify the compression to use for the movie file.

        :param frame_padding: The number of zeros used to pad file name.

        :param image_size: The final image's width and height.  Values larger
            than the dimensions of the active window are clamped.  A width and
            height of ``0`` means to use the window's current size.

        :param launch_viewer: Specify whether a viewer should be launched for
            the playblast.

        :param output_format: The format for the playblast output.

        :param quality: Specify the compression quality factor to use for the
            movie file.  Value should be in the ``0``-``100`` range.

        :param sequence_time: Indicate whether to use sequence time.

        :param show_ornaments: Indicate whether model view ornaments (e.g. the
            axis icon) should be displayed .

        :param view_percent: The percentage of current view size to use during
            blasting.  Accepted values are integers between ``10`` and ``100``.
            All other values are clamped to be within this range.  A value of
            ``25`` means ``1/4`` of the current view size; a value of ``50``
            means half the current view size; a value of ``100`` means full
            size.
        """
        self.__file_path_name = file_path_name

        self.__clear_cache = clear_cache
        self.__compression = compression or self.DEFAULT_COMPRESSION
        self.__frame_padding = frame_padding or self.DEFAULT_FRAME_PADDING
        self.__image_size = image_size or self.DEFAULT_IMAGE_SIZE
        self.__launch_viewer = launch_viewer
        self.__output_format = output_format or self.DEFAULT_OUTPUT_FORMAT
        self.__quality = quality or self.DEFAULT_QUALITY
        self.__sequence_time = sequence_time
        self.__show_ornaments = show_ornaments
        self.__view_percent = view_percent or self.DEFAULT_VIEW_PERCENT

    def build(self) -> str:
        """
        Return the playblast command with its arguments.


        :return: The playblast command and its arguments.
        """
        width, height = self.__image_size

        # For further information about the list of arguments that MEL command
        # `playblast` supports, please consult the following URL:
        #
        #     https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Tech-Docs/Commands/playblast.html#flagquality
        arguments = {
            'clearCache': 1 if self.__clear_cache else 0,
            'compression': f'"{self.__compression}"',
            'filename': f'"{self.__file_path_name}"',
            'format': self.__output_format,
            'framePadding': self.__frame_padding,
            'quality': self.__quality,
            'percent': self.__view_percent,
            'sequenceTime': self.__sequence_time,
            'showOrnaments': 1 if self.__show_ornaments else 0,
            'viewer': 1 if self.__launch_viewer else 0,
            'widthHeight': f'{width} {height}',
        }

        argument_line = ' '.join([f'-{k} {str(v)}' for k, v in arguments.items()])
        command_line = f'playblast {argument_line};'

        return command_line
