ren *.png *.temp
for %%Y in (*.temp) do "Icon Switch.py" "%%Y"
ren *.temp *.png