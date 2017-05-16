# flow-pattern-map
Jupyter Notebook with two-phase flow pattern map calculation.

Please Contact to Dr. Ovadia Shoham by os@utulsa.edu or [Dr. Eduardo Pereyra](https://www.researchgate.net/profile/Eduardo_Pereyra2) for more info about `FlowPat.dll`.

# Installation

    set CONDA_FORCE_32BIT=1
    conda env create
    activate py3_32bit
    
# Before using the notebook

## Disable Data Execution Prevention - DEP (Windows ONLY)

1. Type cmd in the start search menu, **right-click** on it and select **Run as Administrator**.

2. Once the command prompt is open, you can now disable [Data Execution Prevention](https://pt.wikipedia.org/wiki/Data_Execution_Prevention) (DEP) by entering the following command line.

        bcdedit.exe /set nx AlwaysOff

3. And don't forget to enable it back after using it (you may need to restart your machine),

        bcdedit.exe /set nx AlwaysOn
    
