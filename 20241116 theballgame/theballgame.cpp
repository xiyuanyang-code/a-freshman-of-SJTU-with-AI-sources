/*
 * @Author: Xiyuan Yang   xiyuan_yang@outlook.com
 * @Date: 2024-11-11 21:10:21
 * @LastEditors: Xiyuan Yang   xiyuan_yang@outlook.com
 * @LastEditTime: 2024-11-15 23:40:42
 * @FilePath: \CODE_for_Vscode\C++_project\theballgame.cpp
 * @Description: 
 * Do you code and make progress today?
 * Copyright (c) 2024 by Xiyuan Yang, All Rights Reserved. 
 */
#include <iostream>
#include <vector>
using namespace std;
struct ball{
    int v;
    int place;
};



int main(){
    int N,L;cin>>N>>L;
    vector<ball> thestatus;
    thestatus.reserve(N);
    for(int i=0;i<N;i++){
        cin>>thestatus[i].place;
        if(i%2==0){
            thestatus[i].v=1;
        }else{
            thestatus[i].v=-1;
        }
    }
    int thefirstdrop;
    int thelastdrop;
    int time=0;
    int thesucceddcount=0;
    while(thesucceddcount<N){
        time++;
        for(int i=0;i<N;i++){
            thestatus[i].place+=thestatus[i].v;
            if(thestatus[i].place==0||thestatus[i].place==L){
                thesucceddcount++;
                if(thesucceddcount==1){
                    thefirstdrop=time;
                }
                if(thesucceddcount==N){
                    thelastdrop=time;
                }
            }
        }
        for(int i=0;i+1<N;i++){
            if(thestatus[i].place==thestatus[i+1].place){
                swap(thestatus[i].v,thestatus[i+1].v);
            }
        }
    }
    cout<<thefirstdrop<<thelastdrop;
    return 0;
}