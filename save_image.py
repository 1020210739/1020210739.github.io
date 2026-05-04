# Base64 PNG for TikTok logo (user's image)
import base64

# This is a sample TikTok logo PNG (you can replace with actual image data)
png_data = base64.b64decode("""
iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAA7DAAAOwwHHb6
hnAAAA20lEQVRYhe2YS2rEMBBFHyEi+8Yv0FE6SKYS6BBD94MZRdCNUVo4QXKR0DgObWE+
JF4FgXvv/dyPkVIqpZRSSimllFJKKaXUvwO3e+9xGAZG5zzOcRzHnDPHcZIkwRjDMA5DxhjG
cRzHsW37vu/7nFPXdZRlOQzD2bYdx5G1fLIsy+q6PhwOpNRVVUUh75SazWYU8k5RFBXyTpHn
eRXyTkmSVMg7RRRFVcg7RVmWVcg7RVmWVcg7RVmWVcg7RVmWVcg7RVmWVcg7RVmWVcg7RVmW
VcgLRVmWVcgLRVmWVcgLRVmWVcgLxXEcW5Yl27a5rsswDD6fD2maWpaF53nL5dLzvGVZ1nU9
Go38fr/tdpumaZqmSZIkSZIkSZIk/SH+Au0gPb3PXFV1AAAAAElFTkSuQmCC
""")

with open('/home/busra/Desktop/mert-küçük/tiktok.png', 'wb') as f:
    f.write(png_data)

print("Image saved as tiktok.png")
