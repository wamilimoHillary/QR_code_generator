import qrcode

# Define the details
reg_no = "DCMSLMR202922"
name = "GEOFREY MOSE ONYANCHA"
Reg_id = "RG-433889"
program ="DCMS"
stage="Y2S2"
semester = "SEM3/2023-2024"

# Format the details
details = f"Registration No.: {reg_no}; Name: {name}; Reg. ID:: {Reg_id}; Programme : {program}; Stage : {stage}; Semester : {semester}"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(details)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("Dr.wamilimo.png")

print("QR code generated and saved as '.png'")
