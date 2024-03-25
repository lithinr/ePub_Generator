import os
import shutil

if __name__ == '__main__':
    
    #Path where the epub folder needs to be created
    epubbookpath = "C:/Users/lithi/OneDrive/Desktop"
    #Title
    titleofthebook = "നാടന്‍ പ്രേമം"
    titleinenglish ="Naadan Premam"
    #Auther
    autherofthebook = "എസ്‌.കെ. പൊറ്റക്കാട്‌"
    #Publisher 
    publisherofthebook = "Mathrubhoomi Books"
    #language
    languageofthebook = "ml"
    #Unique id
    uniqueidofthebook ="015ffaec-9340-42f8-b163-a0c5ab7d0611"
    #bookstructure
    bookstructure = ["title","prasthavana","chapter01","chapter02","chapter03","chapter04","chapter05","chapter06","chapter07","chapter08","chapter09","chapter10","chapter11","chapter12","chapter13","chapter14","chapter15","chapter16","chapter17","chapter18","chapter19"]
    #chapter names (size should match to bookstructure)
    bookchapternames = [titleofthebook,"പ്രസ്താവന","I","II","III","IV","V","VI","VII","VIII","IX","X","I","II","III","IV","V","VI","VII","VIII","IX"]
    #path the cover image is stored
    coverimagepath = "C:/Users/lithi/My Drive/[04] Personal projects/[04] Epub creations/Naadan_Premam/cover.jpg"





    #Delete folder if existing
    bookpath = os.path.join(epubbookpath,titleinenglish)
    try:
        # Use shutil.rmtree to delete the entire folder and its contents
        shutil.rmtree(bookpath)

        print(f"Folder '{bookpath}' deleted successfully.")
    except FileNotFoundError:
        print(f"Error: Folder '{bookpath}' not found.")
    except PermissionError:
        print(f"Error: Permission denied. Make sure you have the necessary permissions.")
    except Exception as e:
        print(f"Error deleting folder: {e}")


    #Creating book directody
    os.mkdir(bookpath)
    print("Directory created")

    #creating mimetype
    with open(os.path.join(bookpath,"mimetype"),'x') as file:
        file.write("application/epub+zip")
    print("Mimetype created")

    #creating meta-inf and OEBPS
    os.mkdir(os.path.join(bookpath,"META-INF"))
    os.mkdir(os.path.join(bookpath,"OEBPS"))
    
    #creating files inside META-INF
    with open(os.path.join(bookpath,"META-INF","calibre_bookmarks.txt"),'x') as file:
        file.write("calibre_current_page_bookmark*|!|?|*0*|!|?|*/2/4/2/2/1:0")
    with open(os.path.join(bookpath,"META-INF","container.xml"),'x') as file:
        file.write('<?xml version="1.0"?>\n<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n<rootfiles>\n<rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>\n</rootfiles>\n</container>')
    print("Files inside META-INF created")

    #Creating folders inside OEBPS
    os.mkdir(os.path.join(bookpath,"OEBPS","Images"))
    os.mkdir(os.path.join(bookpath,"OEBPS","Styles"))
    os.mkdir(os.path.join(bookpath,"OEBPS","Text"))
    print("Images, Text and Style folders created")

    with open(os.path.join(bookpath,"OEBPS","Styles","stylesheet.css"),'x') as file:
        file.write('/* Style Sheet */\n/* This defines styles and classes used in the book */\nbody { margin-left: 5%; margin-right: 5%; margin-top: 5%; margin-bottom: 5%; text-align: justify; }\npre { font-size: x-small; }\nh1 { text-align: center; }\nh2 { text-align: center; }\nh3 { text-align: center; }\nh4 { text-align: center; }\nh5 { text-align: center; }\nh6 { text-align: center; }\np  { text-indent: 2em; }\n.CI {\n    text-align:center;\n    margin-top:0px;\n    margin-bottom:0px;\n    padding:0px;\n    }\n.center   {text-align: center;}\n.smcap    {font-variant: small-caps;}\n.u        {text-decoration: underline;}\n.bold     {font-weight: bold;}')
    print("stylesheet.css created")

    with open(os.path.join(bookpath,"OEBPS","Styles","page-template.xpgt"),'x') as file:
        file.write('<ade:template xmlns="http://www.w3.org/1999/xhtml" xmlns:ade="http://ns.adobe.com/2006/ade"\nxmlns:fo="http://www.w3.org/1999/XSL/Format">\n\n<fo:layout-master-set>\n<fo:simple-page-master master-name="single_column">\n<fo:region-body margin-bottom="3pt" margin-top="0.5em" margin-left="3pt" margin-right="3pt"/>\n</fo:simple-page-master>\n\n<fo:simple-page-master master-name="single_column_head">\n<fo:region-before extent="8.3em"/>\n<fo:region-body margin-bottom="3pt" margin-top="6em" margin-left="3pt" margin-right="3pt"/>\n</fo:simple-page-master>\n\n<fo:simple-page-master master-name="two_column"    margin-bottom="0.5em" margin-top="0.5em" margin-left="0.5em" margin-right="0.5em">\n<fo:region-body column-count="2" column-gap="10pt"/>\n</fo:simple-page-master>\n\n<fo:simple-page-master master-name="two_column_head" margin-bottom="0.5em" margin-left="0.5em" margin-right="0.5em">\n<fo:region-before extent="8.3em"/>\n<fo:region-body column-count="2" margin-top="6em" column-gap="10pt"/>\n</fo:simple-page-master>\n\n<fo:simple-page-master master-name="three_column" margin-bottom="0.5em" margin-top="0.5em" margin-left="0.5em" margin-right="0.5em">\n<fo:region-body column-count="3" column-gap="10pt"/>\n</fo:simple-page-master>\n\n<fo:simple-page-master master-name="three_column_head" margin-bottom="0.5em" margin-top="0.5em" margin-left="0.5em" margin-right="0.5em">\n<fo:region-before extent="8.3em"/>\n<fo:region-body column-count="3" margin-top="6em" column-gap="10pt"/>\n</fo:simple-page-master>\n\n<fo:page-sequence-master>\n<fo:repeatable-page-master-alternatives>\n<fo:conditional-page-master-reference master-reference="three_column_head" page-position="first" ade:min-page-width="80em"/>\n<fo:conditional-page-master-reference master-reference="three_column" ade:min-page-width="80em"/>\n<fo:conditional-page-master-reference master-reference="two_column_head" page-position="first" ade:min-page-width="50em"/>\n<fo:conditional-page-master-reference master-reference="two_column" ade:min-page-width="50em"/>\n<fo:conditional-page-master-reference master-reference="single_column_head" page-position="first" />\n<fo:conditional-page-master-reference master-reference="single_column"/>\n</fo:repeatable-page-master-alternatives>\n</fo:page-sequence-master>\n\n</fo:layout-master-set>\n\n<ade:style>\n<ade:styling-rule selector=".title_box" display="adobe-other-region" adobe-region="xsl-region-before"/>\n</ade:style>\n\n</ade:template>')
    print("page-template.xpgt created")



    #creating toc.ncx
    with open(os.path.join(bookpath,"OEBPS","toc.ncx"),'x',encoding='utf-8') as file:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN"\n   "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">\n\n<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">\n    <head>\n        <meta name="dtb:uid" content="'+uniqueidofthebook+'"/>\n        <meta name="dtb:depth" content="2"/>\n        <meta name="dtb:totalPageCount" content="0"/>\n        <meta name="dtb:maxPageNumber" content="0"/>\n    </head>\n    <docTitle>\n        <text>'+titleofthebook+'</text>\n    </docTitle>\n    <navMap>\n')
        count =0
        for chapters in bookstructure:
            file.write('        <navPoint id="'+chapters+'.xhtml" playOrder="'+str(count+1)+'">\n                <navLabel>\n                    <text>'+bookchapternames[count]+'</text>\n                </navLabel>\n                <content src="Text/'+chapters+'.xhtml"/>\n        </navPoint>\n')
            count = count+1
        file.write('    </navMap>\n</ncx>')
    print("toc.ncx created")
    
    
    #creating content.opf
    with open(os.path.join(bookpath,"OEBPS","content.opf"),'x',encoding='utf-8') as file:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookID" version="2.0">\n    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">\n        <dc:title>'+titleofthebook+'</dc:title>\n        <dc:language>'+languageofthebook+'</dc:language>\n        <dc:rights>Public Domain</dc:rights>\n        <dc:creator opf:role="aut">'+autherofthebook+'</dc:creator>\n        <dc:publisher>'+publisherofthebook+'</dc:publisher>\n        <dc:identifier id="BookID" opf:scheme="UUID">'+uniqueidofthebook+'</dc:identifier>\n        <meta name="Sigil version" content="0.2.4"/>\n        <meta name="cover" content="cover.jpg"/>\n    </metadata>\n    <manifest>\n        <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>\n        <item id="cover.jpg" href="Images/cover.jpg" media-type="image/jpeg"/>\n        <item id="page-template.xpgt" href="Styles/page-template.xpgt" media-type="application/vnd.adobe-page-template+xml"/>\n        <item id="stylesheet.css" href="Styles/stylesheet.css" media-type="text/css"/>\n        <item id="cover.xhtml" href="Text/cover.xhtml" media-type="application/xhtml+xml"/>\n')
        for chapters in bookstructure:
            file.write('        <item id="'+chapters+'.xhtml" href="Text/'+chapters+'.xhtml" media-type="application/xhtml+xml"/>\n')
        file.write('    </manifest>\n    <spine toc="ncx">\n        <itemref idref="cover.xhtml"/>\n')
        for chapters in bookstructure:
            file.write('        <itemref idref="'+chapters+'.xhtml"/>\n')
        file.write('    </spine>\n</package>')
    print("content.opf created")

    #Creating title page
    with open(os.path.join(bookpath,"OEBPS","Text","title.xhtml"),'x',encoding='utf-8') as file:
        file.write('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"\n  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">\n\n<html xmlns="http://www.w3.org/1999/xhtml">\n	<head>\n		<title>'+titleofthebook+'</title>\n		<link rel="stylesheet" href="../Styles/stylesheet.css" type="text/css" />\n		<link rel="stylesheet" type="application/vnd.adobe-page-template+xml" href="../Styles/page-template.xpgt" />\n	</head>\n	<body>\n		<div>\n			<p>&nbsp;</p>\n			<h3 id="heading_id_1">'+autherofthebook+'</h3>\n			<h2 id="heading_id_2">'+titleofthebook+'</h2>\n		</div>\n	</body>\n</html>')
    print("title.xhtml created")

    #Copying cover image
    shutil.copy(coverimagepath, os.path.join(bookpath,"OEBPS","Images"))
    print("cover image copied")

    #Creating cover page
    with open(os.path.join(bookpath,"OEBPS","Text","cover.xhtml"),'x',encoding='utf-8') as file:
        file.write('<?xml version="1.0" encoding="utf-8"?>\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">\n	<head>\n		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>\n		<meta name="calibre:cover" content="true"/>\n		<title>Cover</title>\n		<style type="text/css" title="override_css">\n			@page {padding: 0pt; margin:0pt}\n			body { text-align: center; padding:0pt; margin: 0pt; }\n		</style>\n	</head>\n	<body>\n		<div>\n			<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="100%" height="100%" viewBox="0 0 1600 2560" preserveAspectRatio="none">\n				<image width="1600" height="2560" xlink:href="../Images/cover.jpg"/>\n			</svg>\n		</div>\n	</body>\n</html>' )
    print("cover.xhtml created")
    
    #Creating all the chapter xhtmls
    count =0
    for chapters in bookstructure:
            if count>0:
                filename = chapters + ".xhtml"
                with open(os.path.join(bookpath,"OEBPS","Text",filename),'x',encoding='utf-8') as file:
                    file.write('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"\n  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">\n\n<html xmlns="http://www.w3.org/1999/xhtml">\n	<head>\n		<title>'+bookchapternames[count]+'</title>\n		<link rel="stylesheet" href="../Styles/stylesheet.css" type="text/css" />\n		<link rel="stylesheet" type="application/vnd.adobe-page-template+xml" href="../Styles/page-template.xpgt" />\n	</head>\n	<body>\n		<div>\n			<h3 id="heading_id_2">'+bookchapternames[count]+'</h3>\n				<p></p>\n		</div>\n	</body>\n</html>')
            count = count+1
    print("All xhtmls created")
    