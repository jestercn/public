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
        // ������һ�б�ͷ
        std::getline(inputFile, line);

        while (std::getline(inputFile, line)) {
            std::istringstream iss(line);
            std::string oldName, newName;
            // ����ÿ��������������ɣ�ʹ�ö�����Ϊ�ָ���
            std::getline(iss, oldName, ',');
            std::getline(iss, newName, ',');

            fileData.push_back({ oldName, newName });
        }

        inputFile.close();
    } else {
        std::cout << "�޷���csv�����ļ�: " << filename << std::endl;
    }

    return fileData;
}

int renameFiles(const std::vector<FileData>& fileData) {
    std::ofstream f;
	f.open("out_result.csv",std::ios::out);
    for (const auto& data : fileData) {
        if (std::rename(data.oldName.c_str(), data.newName.c_str()) != 0) {
            std::cout << "�������ļ�ʧ�ܣ�" << data.oldName << std::endl;
            f<<data.oldName<<std::endl;
            cnt++;
        }
    }
    f.close();
    return cnt;
}

int main() {
    std::cout<<"**********���ñ���������ݶ��ļ�����������(���ֶ�������)**********"<<std::endl;
    std::cout<<"����������ļ���������չ�� #: ";
    std::string csv_file;
    std::cin>>csv_file;
    std::string filename = csv_file;  // ��������ļ���

    // �����ļ�����
    std::vector<FileData> fileData = parseFileData(filename);

    // ִ������������
    if (!renameFiles(fileData)) {
        std::cout << "�����ļ��ѳɹ���������" << std::endl;
    }else{
        std::cout <<cnt<<"���ļ�������ʧ��"<<std::endl;
    }
    std::cout<<"�������˳����� #: "<<std::endl;
    while(std::cin>>cnt && (cnt!=999)){
        std::cout<<"���벻��ȷ,���������� #: "<<std::endl;
    }
    return 0;
}
