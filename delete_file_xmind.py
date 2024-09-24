import os
import send2trash
from datetime import datetime

# 设置要处理的目录和日志文件
target_dir = r"<xmind file cache path >"  #your xmind path is usually : C:\Users\< userName >\AppData\Roaming\Xmind\Electron v3\vana\file-cache
log_file = r"<your log file path with name deleted_files_log_xmind >" #your log file path, make sure you have create the txt file(eg. deleted_files_log_xmind.txt)

# 清空日志文件
with open(log_file, 'w') as f:
    f.write("")

# 总删除计数
total_deleted = 0

# 遍历所有子文件夹
for root, dirs, files in os.walk(target_dir):
    if len(files) > 5:
        # 记录当前文件夹
        folder_path = root
        # 获取文件的完整路径和修改时间
        files_with_time = [
            (os.path.join(root, file), os.path.getmtime(os.path.join(root, file)))
            for file in files
        ]
        
        # 按修改时间排序（最新的在前）
        files_with_time.sort(key=lambda x: x[1], reverse=True)

        # 计算需要删除的文件数量
        files_to_delete = files_with_time[5:]
        counter = 0

        for file_path, _ in files_to_delete:
            try:
                # 移动文件到回收站
                send2trash.send2trash(file_path)
                # 获取当前时间
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(log_file, 'a') as f:
                    f.write(f"{now} - Deleted: {file_path}\n")
                counter += 1
                total_deleted += 1
            except Exception as e:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(log_file, 'a') as f:
                    f.write(f"{now} - Failed to delete {file_path}: {str(e)}\n")

        # 输出已删除文件的数量
        with open(log_file, 'a') as f:
            f.write(f"Deleted {counter} files from {folder_path}\n")

# 记录总删除数量
with open(log_file, 'a') as f:
    f.write(f"Total deleted files: {total_deleted}\n")
