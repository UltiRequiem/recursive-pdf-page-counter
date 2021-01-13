# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\eliaz\\Desktop\\Repositorios\\PDF_to_CSV-with-Python\\Source\\src\\main\\python\\main.py'],
             pathex=['C:\\Users\\eliaz\\Desktop\\Repositorios\\PDF_to_CSV-with-Python\\Source\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['c:\\programdata\\miniconda3\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['C:\\Users\\eliaz\\Desktop\\Repositorios\\PDF_to_CSV-with-Python\\Source\\target\\PyInstaller\\fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='PdfToCsv',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='C:\\Users\\eliaz\\Desktop\\Repositorios\\PDF_to_CSV-with-Python\\Source\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='PdfToCsv')
