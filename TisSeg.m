clc; clear all

addpath('/home/miranda/Documents/MATLAB/spm12')
spm('defaults', 'FMRI');

dataDir = '/home/miranda/Documents/code/official/ClinicalCTSeg';
% subject list
filename = '/home/miranda/Documents/data/INSPIRE/subtype/v1022.txt';
fid=fopen(filename);
file_list = {};
tline = fgetl(fid);
n = 0;
while ischar(tline)
    n = n+1;
    disp(tline)
    [filepath,name,ext] = fileparts(tline)
    file_list{n}=filepath
    tline = fgetl(fid);
end
fclose(fid);

list_f = {'/home/miranda/Documents/data/INSPIRE/subtype/V10.2/INSP_CN020085_10033612/1405357_1644606/CT_1_Cere_30000013031210434937500000105',
 	'/home/miranda/Documents/data/INSPIRE/subtype/V10.2/INSP_AU010331_0810425/21665_2066981201_1145702815/CT_8206_NON__1145706856'}
list_f = reshape(list_f, 1, 2);	

% for subj = file_list
for subj = list_f
    % display the subject (not necessary, but helpful)
    disp(strcat('Subject:   ',subj));
    % clear matlabbatch variables 
    clear matlabbatch;
     % cd into the subject directory.
    cd(char(subj));
    % call the job nrm1_job.m
    try
        spm_jobman('run','/home/miranda/Documents/code/official/ClinicalCTSeg/TisSeg_job.m')
    catch e
        fprintf(1,'The identifier was:\n%s',e.identifier);
        fprintf(1,'There was an error! The message was:\n%s',e.message);
    end
    % When finished, go back up to the dataDir
    cd(dataDir)
end
