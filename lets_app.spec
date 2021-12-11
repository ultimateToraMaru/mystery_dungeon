# -*- mode: python ; coding: utf-8 -*-

### pyxelを認識するためのコード ###
import sys
myLibPath = './libs'
sys.path.append(myLibPath)
############################


block_cipher = None


a = Analysis(
    ['app.py'],
    pathex=['C:/Users/nekok/OneDrive/ドキュメント/MyHobby/Programming/Python/mystery_dungeon'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    Tree('assets',prefix='assets'), #<--追加するイメージがあるフォルダ名
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='MysteryDungeon',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
