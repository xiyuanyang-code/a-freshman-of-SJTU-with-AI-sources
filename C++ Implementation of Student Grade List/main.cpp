/*
 * @Author: Xiyuan Yang   xiyuan_yang@outlook.com
 * @Date: 2024-11-28 20:35:19
 * @LastEditors: Xiyuan Yang   xiyuan_yang@outlook.com
 * @LastEditTime: 2024-11-28 23:22:07
 * @FilePath: \CODE_for_Vscode\C++_project\thegradelist.cpp
 * @Description:
 * Do you code and make progress today?
 * Copyright (c) 2024 by Xiyuan Yang, All Rights Reserved.
 */
#include <iostream>

#include "thestudent.h"
using namespace std;



int main(){
    vector<student> students;
    cout<<"Hello!"<<endl;
    int operate;
    while (true) {
        printthemenu();
        cin>>operate;
        assert(operate<0||operate>13);
        if (!operate) {
            cout<<"Exit Successfully!"<<endl;
            break;
        }else {

        }
    }
    return 0;
}
