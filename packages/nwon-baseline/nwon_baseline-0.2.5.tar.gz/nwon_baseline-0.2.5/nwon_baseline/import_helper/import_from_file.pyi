from nwon_baseline.print_helper import print_color as print_color
from nwon_baseline.typings.terminal_colors import TerminalColors as TerminalColors
from typing import List, Optional

def import_data_from_file(path: str, split_character: str, expected_column_names: List[str]) -> Optional[List[List[str]]]: ...
