#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <ctime>
int cnt;
struct FileData {
    std::string oldName;
    std::string newName;
};

std::vector<FileData> parseFileData(const std::string& filename) {
    std::vector<FileData> fileData;
    std::ifstream inputFile(filename);

    if (inputFile.is_open()) {
        std::string line;
        // 跳过第一行表头
        std::getline(inputFile, line);

        while (std::getline(inputFile, line)) {
            std::istringstream iss(line);
            std::string oldName, newName;
            // 假设每行数据由两列组成，使用逗号作为分隔符
            std::getline(iss, oldName, ',');
            std::getline(iss, newName, ',');

            fileData.push_back({ oldName, newName });
        }

        inputFile.close();
    } else {
        std::cout << "无法打开csv输入文件: " << filename << std::endl;
    }

    return fileData;
}

int renameFiles(const std::vector<FileData>& fileData) {
    std::ofstream f;
	f.open("out_result.csv",std::ios::out);
    for (const auto& data : fileData) {
        if (std::rename(data.oldName.c_str(), data.newName.c_str()) != 0) {
            std::cout << "重命名文件失败：" << data.oldName << std::endl;
            f<<data.oldName<<std::endl;
            cnt++;
        }
    }
    f.close();
    return cnt;
}

int main() {
    std::cout<<"**********利用表格两列内容对文件进行重命名(带字段名首行)**********"<<std::endl;
    std::cout<<"请输入表格的文件名包括扩展名 #: ";
    std::string csv_file;
    std::cin>>csv_file;
    std::string filename = csv_file;  // 表格数据文件名

    // 解析文件数据
    std::vector<FileData> fileData = parseFileData(filename);

    // 执行重命名操作
    if (!renameFiles(fileData)) {
        std::cout << "所有文件已成功重命名！" << std::endl;
    }else{
        std::cout <<cnt<<"个文件重命名失败"<<std::endl;
    }
    std::cout<<"请输入退出密码 #: "<<std::endl;
    while(std::cin>>cnt && (cnt!=999)){
        std::cout<<"密码不正确,请重新输入 #: "<<std::endl;
    }
    return 0;
}
