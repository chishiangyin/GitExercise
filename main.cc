#include <iostream>
#include "TFile.h"
#include "TH1.h"
#include "TH1F.h"
#include "TH1D.h"
#include <string>
#include <fstream>
#include <vector>

int main() 
{
    Double_t boundary[102];
    boundary[0] = 0;
    boundary[1] = 0.05;

    for(int i=2; i<102; i++) 
    {
        boundary[i] = boundary[i-1] + 0.1;
    }
        
    TH1D* h_Two_Methods_Ratio = new TH1D("h_Two_Methods_Ratio","",101,boundary);
    h_Two_Methods_Ratio->GetXaxis()->SetTitle("E[MeV]"); 

    for(int i=0; i<101; i++)
    {
        h_Two_Methods_Ratio->SetBinContent(i+1,0);
    }
        
    std::ifstream readin_1("/junofs/users/yinqixiang/SummationSpectrum/files/bin_method_1.txt");
    std::ifstream readin_2("/junofs/users/yinqixiang/SummationSpectrum/files/bin_method_2.txt");
    std::string read_line_1, read_line_2;
    std::vector<double> read_1, read_2;
    while(std::getline(readin_1,read_line_1))
    {
        read_1.push_back(stod(read_line_1));
    }
    while(std::getline(readin_2,read_line_2))
    {
        read_2.push_back(stod(read_line_2));
    }
    for(int i=1; i<=101; i++)
    {
        h_Two_Methods_Ratio->SetBinContent(i,read_1[i-1]/read_2[i-1]);
    }

    TFile* outfile = new TFile("ratio.root", "RECREATE");
    outfile->cd();
    h_Two_Methods_Ratio->Write();
    outfile->Close();
    return 0;
}
