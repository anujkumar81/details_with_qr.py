import qrcode
qr_image = qrcode.make("Hello, Thanks For reaching Out to 'ANUJ KUMAR' ")
print("THIS IS ABOUT ME.")
print("Name:            Anuj Kumar"
      "Mob_No:          822xxxx981"
      "Email:           anujkumarcse2025@scteng.co.in"
      "Location:         38, SAran,Bihar- 841101"
)
qr_image.save("qr_image.jpg")