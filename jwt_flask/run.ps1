# Convenience development run script for Windows/Powershell

$Env:FLASK_APP = "jwtapp"
$Env:FLASK_DEBUG = "1"

$Host.UI.RawUI.WindowTitle = "jwtapp"

# launch the server
python -m flask run --reload --debugger --with-threads
