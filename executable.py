import PyInstaller.__main__

PyInstaller.__main__.run([
    'src/main.py',
    '--onefile',
    '--windowed',
    "--icon=assets\\business_table_order_report_history_2332.ico"
])