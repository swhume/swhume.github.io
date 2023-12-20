# Generating Define-XML v2.1 using odmlib

I introduced odmlib, an open-source Python library for working with ODM, in my first blog post by providing a bit of 
background and walking through the creation of an ODM "hello, world" equivalent. In this post, I’ll walk through the 
highlights of generating a Define-XML v2.1 document using odmlib and a spreadsheet containing the metadata.

For many in the CDISC community, working with Define-XML represents how they work with the CDISC Data Exchange 
Standards. In this blog post I will highlight two odmlib example programs that work with Define-XML v2.1:

* **xlsx2define2-1.py** generates a Define-XML v2.1 XML document using the odmlib-define-metadata.xlsx spreadsheet 
containing example metadata
* **Define-2-1-to-xlsx.py** generates a metadata spreadsheet from a Define-XML v2.1 XML document

These simple example programs highlight a common use case: generating Define-XML from a metadata spreadsheet. 
These example programs can be enhanced to add new features, or the knowledge gained from these examples can be applied 
towards creating a more sophisticated odmlib-based Define-XML application.

## Getting Started
To get started, download the odmlib examples from the 
[odmlib_examples repository on my GitHub site](https://github.com/swhume/odmlib_examples). The 
requirements.txt file references odmlib, in addition to the other libraries required by the example programs, but you 
may also install odmlib manually using pip.

```
pip install odmlib
```
Python 3.8 was used to develop the two Define-XML v2.1 examples, though a number of other recent versions should work.

Let’s start with running xlsx2define2-1.py with the example spreadsheet included in the project’s data directory.
```
python xlsx2define2-1.py -e ./data/odmlib-define-metadata.xlsx -d ./data/odmlib-roundtrip-define.xml
```
The -e indicates the Excel file that contains the metadata and the -d the Define-XML v2.1 file to create. If Python 
and the required libraries are installed correctly, the above command-line should generate the 
odmlib-roundtrip-define.xml file in the data directory using the metadata provided in the spreadsheet.

## Checking Your Define-XML Output
Once you’re able to run the example application to generate the Define-XML output, you can take the next step and check 
the Define-XML output against the schema and some basic conformance checks. To do this, add the -v to validate the 
output and include the -s to provide the path and filename of the Define-XML v2.1 schema. The schema is not included 
with the examples, so you will need to change the path in the reference below to point to the schema on your system. 
If you don’t have the schema on your system, download it from the 
[Define-XML page on the CDISC web site](https://www.cdisc.org/standards/data-exchange/define-xml). The following 
command-line example shows the addition of both schema validation and basic conformance checking to the Define-XML 
generation.
```
python xlsx2define2-1.py -v -c
    -e ./data/odmlib-define-metadata.xlsx 
    -d ./data/odmlib-roundtrip-define.xml
    -s /DefineV211/schema/cdisc-define-2.1/define2-1-0.xsd
```

## Generating a Spreadsheet From Define-XML v2.1
Now that you’ve seen how to generate a Define-XML v2.1 file from a metadata spreadsheet, next I’ll cover how to 
generate the metadata spreadsheet from Define-XML using the define2-1-to-xlsx.py example application.

The define2-1-to-xlsx.py application uses -d to indicate the Define-XML v2.1 file and -p for the path to the Excel file. 
This application generates an Excel file named odmlib-define-metadata.xlsx. Given the odmlib-roundtrip-define.xml file 
provided in the data directory of the example program, or given the same file you just created by running the previous 
example program, the application generates the metadata spreadsheet. The following command-line example demonstrates 
this.
```
python define2-1-to-xlsx.py -d ./data/odmlib-roundtrip-define.xml -p ./data/
```

You can opt to validate the Define-XML before generating the spreadsheet by again adding the -v for validation and the 
-s for the path to the Define-XML v2.1 schema.
```
python define2-1-to-xlsx.py -d ./data/odmlib-roundtrip-define.xml -p ./data/ -v -s /DefineV211/schema/cdisc-define-2.1/define2-1-0.xsd
```

You could also go roundtrip and re-generate the Define-XML v2.1 from the new metadata spreadsheet using the 
xlsx2define2-1.py example program.

## Next Steps
This post introduces two odmlib example applications that demonstrate the generation of Define-XML v2.1 from a metadata 
spreadsheet. These are example applications meant to demonstrate the basics of using the odmlib library.

These are simple example programs that have not been widely tested yet, but you can change or add new metadata rows to 
the existing worksheets and columns to generate your own Define-XML v2.1 file.

If you want to add your own worksheets and columns we’ll need to dig into the code. We’ll walk through making the code 
changes needed to add a worksheet or column in a future blog post.
