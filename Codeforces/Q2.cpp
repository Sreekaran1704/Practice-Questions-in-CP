#include <bits/stdc++.h>
using namespace std;

int main(){
    string a,b,a1="",b1="";
    int m,n;
    cin>>a;
    cin>>b;
    for(int i=0;i<a.size();i++){
        a1=a1+(char)tolower(a[i]);
    }
    for(int i=0;i<b.size();i++){
        b1=b1+(char)tolower(b[i]);
    }
    const char *c = a1.c_str();
    const char *d = b1.c_str();
    m = a.length();
    n = b.length();
    if(strcmp(c,d)==0){
        cout<<0;
    }else if(strcmp(c,d)>0){
        cout<<1;
    }else{
        cout<<-1;
    }
}