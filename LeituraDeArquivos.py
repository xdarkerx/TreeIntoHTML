import os
import html
from pathlib import Path

def tree_to_html(root, folder):
    result = ""
    folder_path = Path(folder)
    if folder_path.is_dir():
        num_files = len(list(folder_path.iterdir()))
        result += "<ul class='list-group open'>\n"
        for path in folder_path.iterdir():
            if path.exists() and path.is_dir():
                try:
                    os.chdir(path)
                except PermissionError:
                    continue
                except FileNotFoundError:
                    continue
                subfiles = list(path.iterdir())
                num_subfiles = len(subfiles)
                result += "<li class='list-group-item list-group-item'>" + html.escape(path.name) + " (" + str(num_subfiles) + " - Itens dentro da pasta)"
                result += "<a href='#' class='toggle'>+</a>\n"
                try:
                    result += tree_to_html(root, str(path))
                except FileNotFoundError:
                    continue
                os.chdir('..')
            elif path.exists() and path.is_file():
                try:
                    result += "<li class='list-group-item'>" + html.escape(path.name) + "</li>\n"
                except FileNotFoundError:
                    continue
        result += "</ul>\n"
    return result

  
# Exemplo de uso:
root = r"C:/Users/"
html_tree = tree_to_html(root, root)

# Adiciona Bootstrap e CSS personalizado ao arquivo HTML
css = """
ul.list-group.open {
  display: block;
}
ul.list-group ul {
  display: none;
}
a.toggle:before {
  content: "+";
  display: inline-block;
  width: 8px;
  height: 8px;
  margin-right: 5px;
  margin-top: -1px;
  text-align: center;
  font-weight: bold;
  font-size: 14px;
  line-height: 8px;
  color: #fff;
  background-color: #ccc;
  border-radius: 50%;
}
a.toggle:before {
  content: "+";
}
"""

with open("C:/Users/tree.html", "w", encoding="utf-8") as f:
    f.write("<html>\n<head>\n")
    f.write("<meta name='viewport' content='width=device-width, initial-scale=1'>\n")
    f.write("<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css'>\n")
    f.write("<style>\n")
    f.write(css)
    f.write("</style>\n</head>\n<body>\n")
    f.write("<div class='container'>\n")
    f.write(html_tree)
    f.write("</div>\n")
    f.write("<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js'></script>\n")
    f.write("<script src='https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js'></script>\n")
    f.write("<script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js'></script>\n")
    f.write("<script>\n")
    f.write("""
      $(document).ready(function(){
        $('a.toggle').click(function(e){
          e.preventDefault();
          $(this).parent().children('ul').toggleClass('open');
          $(this).toggleClass('open');
        });
      });
    """)
    f.write("</script>\n")
    f.write("</body>\n</html>\n")
