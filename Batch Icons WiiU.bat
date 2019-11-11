ren *.png *.temp
for %%Y in (*.temp) do "Icon WiiU.py" "%%Y"
ren *.temp *.png