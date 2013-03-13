import copper
# copper.r.install_packages()

copper.project.path = '..'
ds = copper.load('cleaned')

print ds

copper.r.impute(ds)