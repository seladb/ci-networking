:: Install WinPcap Runtime
git submodule update --init --recursive
git clone https://github.com/mfontanini/winpcap-installer.git
winpcap-installer\winpcap-boundary-meter-4.1.3.exe /S
rmdir winpcap-installer /s /q
