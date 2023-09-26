import winreg

# Open the Windows Registry
reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced")

# Disable Home and OneDrive options in the sidebar
winreg.SetValueEx(reg_key, "NavPaneShowHomeGroup", 0, winreg.REG_DWORD, 0)
winreg.SetValueEx(reg_key, "NavPaneShowOneDrive", 0, winreg.REG_DWORD, 0)

# Close the Registry key
winreg.CloseKey(reg_key)
