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


        :param file_path_name:
        :param clear_cache:
        :param compression:
        :param frame_padding:
        :param image_size:
        :param launch_viewer:
        :param output_format:
        :param quality:
        :param sequence_time:
        :param show_ornaments:
        :param view_percent:
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
