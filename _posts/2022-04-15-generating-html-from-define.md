# Generating HTML from Define-XML

This blog post describes an an open-source, command-line method to convert Define-XML to HTML using the define2-1 
stylesheet

Recently, a few folks have asked for a simple way to convert a Define-XML to HTML without requiring the purchase of a 
software tool. These questions may be triggered by the fact that modern browsers do not transform local XML files 
using XSLT due to security concerns. IE11 is the last major browser to that transforms a local Define-XML document to 
HTML using an XSLT stylesheet reference, and as of 15-Jun-2022 IE11 will no longer be supported.

I often use the Oxygen XML editing software to convert XML files like Define-XML to HTML. Oxygen is not expensive, 
but it is a developer’s tool that may be overkill if your only need is to transform a Define-XML file to HTML. 
A well-known and widely used XSLT processor is available as open-source and also happens to be an XSLT processor 
used by Oxygen.

A simple, open-source approach to converting Define-XML to HTML is to use the Saxon XSLT and XQuery Processor with 
the define2-1.xsl style sheet created by Lex Jansen. The Saxon HE version is available as open-source. 
The following instructions list the steps to installing and running Saxon to transform your Define-XML document into 
an HTML rendering.

### 1. Make sure you have Java installed on your computer.

I find most computers already have Java installed. If not, download from Oracle and install. You can use the 
command-line to test your computer for Java
```
>java -version
```
If Java is installed and accessible you will see output similar to:
```
java version "1.8.0_31"
Java(TM) SE Runtime Environment (build 1.8.0_31-b13)
Java HotSpot(TM) Client VM (build 25.31-b07, mixed mode, sharing)
```
If Java is not installed or accessible you will see output similar to:
```
'java' is not recognized as an internal or external command, operable program or batch file.
```
					
Here’s a link to the Oracle instructions for installing Java on Windows: 
[Java download](https://www.java.com/en/download/help/windows_manual_download.html)

### 2. Download the open-source Saxon XSLT and XQuery Processor from SourceForge.

* You can find the project on SourceForge here: [Saxon download](https://sourceforge.net/projects/saxon/).

* Place the saxon .zip file anywhere on your hard disk - ideally somewhere easy to access to via command-line.

* Do not place it in /Library/Java/Extensions or in UserName/Library/Java/Extensions or in a folder whose name 
contains a /

* NOTE: Lex Jansen has included a version of Saxon in his GitHub repository and you can use that instead of downloading 
Saxon separately. We'll work with Lex's GitHub repository in the next step.

### 3. Clone the define2-1.xsl stylesheet from the Lex Jansen’s GitHub repository.
* You can find the project on the COSA Directory
* You can find instructions on cloning a GitHub repository here: 
[Cloning a Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
* Put the define2-1.xsl stylesheet in a directory easily accessible from the command-line.
* The command to clone the GitHub repository is:
```
git clone https://github.com/lexjansen/define-xml-2.1-stylesheets.git
```

### 4. Generate your Define-xml file in a directory easily accessible from the command-line.

### 5. Run saxon to transform the XML into HTML using the stylesheet
* The command-line to transform the Define-XML document to HTML:
```
>java -jar 'path/to/saxon-he-11.1.jar' -xsl:'path/to/define2-1.xsl' -s:'path/to/define.xml' -o:'path/to/define.html'
```
* The version of the saxon .jar file may be higher, so adjust as needed. Obviously, you will need to adjust the paths 
and path formats to match your environment.
* Double-click on the newly generated HTML file (e.g. define.html) to view it in the browser.

Although there are 5 steps in the above instructions, all but one are used once to setup your system to run the 
transformations. Once you have your computer setup to run Saxon with the define2-1.xls stylesheet, just use 
command-line in Step 5 to repeat the transformation.

NOTE: This is one way to generate an HTML rendering of the Define-XML using the published stylesheet, but there are 
other methods worthy of consideration.
