import os
from PIL import Image


def main():
    image_path_list = [
        "C:\\Users\\ericw\\Downloads\\103077708_502182510500094_2807929953103394283_n.png",
    ]

    image_list = [
        Image.open(image_path).convert('RGB') for image_path in image_path_list
    ]

    first_image, *remaining_image_list = image_list

    result_pdf_folder = "{}\\{}".format(
        os.path.dirname(os.path.realpath(__file__)),
        "Result PDFs"
    )
    pdf_name = "{}.pdf".format(
        "result_pdf"
    )

    save_path = "{}\\{}".format(
        result_pdf_folder,
        pdf_name
    )
    first_image.save(save_path, save_all=True, append_images=remaining_image_list)


main()
