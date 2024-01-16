import os
import shutil

CURRENT_DIR = os.getcwd()
INPUT_FILE_DIR = os.path.join(CURRENT_DIR, 'files')

def excpect_catch_deco(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print(f"{args[0]}が見つかりません。")
        except PermissionError:
            print(f"{args[0]}の権限がありません。")
        except Exception as e:
            print(f"エラーが発生しました: {str(e)}")
    return wrapper


@excpect_catch_deco
def reverse_file(target_filename, output_filename):
    """ファイル内容を逆にした新しいファイル作成"""

    contents = ''
    output_file_path = os.path.join(INPUT_FILE_DIR, output_filename)

    with open(os.path.join(INPUT_FILE_DIR, target_filename)) as f:
        contents = f.read()[::-1]
    
    with open(output_file_path, 'w') as fw:
        fw.write(contents)

    print(f'ファイルの作成が完了しました。{output_file_path}')

@excpect_catch_deco
def copy_file(target_filename, output_filename):
    """ファイルをコピー"""

    source_file_path = os.path.join(INPUT_FILE_DIR, target_filename)
    _output_filename = os.path.join(INPUT_FILE_DIR, output_filename)
    shutil.copy(source_file_path, _output_filename)

    print(f'ファイルのコピーが完了しました。 {_output_filename}')

@excpect_catch_deco
def add_duplicate_content(target_filename, count):
    """ファイルの内容をn回複製する"""

    contents = ''
    target_path = os.path.join(INPUT_FILE_DIR, target_filename)
    with open(target_path, 'r+') as f:
        contents = f.read()
        for _ in range(count):
            f.write('\n')
            f.write(contents)

    print(f'ファイルの追加が完了しました。 {target_path}')

@excpect_catch_deco
def relpace_str_in_file_content(target_filename, target_str, new_str):
    """ファイルの中身から特定の内容を置換する"""

    contents = ''
    target_filename = os.path.join(INPUT_FILE_DIR, target_filename)

    with open(target_filename, 'r+') as f:
        contents = f.read()
        f.seek(0)
        f.write(contents.replace(target_str, new_str))

    print(f'ファイル内容の修正が完了しました。 {target_filename}')

def execute_command(command_arg):
    match command_arg.split():
        case ["reverse", target_filename, output_filename]:
            reverse_file(target_filename, output_filename)
        case ["copy", target_filename, output_filename]:
            copy_file(target_filename, output_filename)
        case ["duplicate-content", target_filename, n]:
            add_duplicate_content(target_filename, count=int(n))
        case ["replace-string", target_filename, target_str, new_str]:
            relpace_str_in_file_content(target_filename, target_str, new_str)
        case ["quit" | "exit" | "bye"]:
            print("プログラム終了")
            quit()
        case _:
            print(f"その様なコマンドは存在しません。: {command_arg}.")

def main():
    while True:
        print('コマンドを入力してください。')
        command_arg = input()
        execute_command(command_arg)

if __name__ == '__main__':
    print('カレントディレクトリにあるfilesフォルダに対象ファイルを配置してください。')
    print('以下のコマンドが有効です。')
    print('reverse 対象ファイル名 出力ファイル名')
    print('copy 対象ファイル名 出力ファイル名')
    print('duplicate-content 対象ファイル名 反復回数')
    print('replace-string 対象ファイル名 変換対象 変換対象後')
    print('quit, exit, bye でプログラムを終了します。')
    main()
