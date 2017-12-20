## 环境:
   - pro engineer 5.0 M090
   - jdk 1.4.1
   - jre 1.7.1

安装的时候必须额外勾选jlink模块以及jre模块。


## 环境变量配置

`CLASSPATH`: jdk-path;jlink-project-path;pfc-path;%CLASSPATH%

`PATH`:  %PATH%;pfc-pah;project-jre-path;jdk-path;

`JAVA_HTOME`: jdk-path;

`PRO_COMM_MSG_EXE`: {{install-path}}/{{platform}}/obj/pro_comm_msg.exe

`PRO_DIRECTORY`: {{install-pah}}


## 注册文件 `protk.dat`

```
# 07-Feb-00  I-03-26  $$1 JCN Changed class name.
# 20-Nov-02  J-03-38  $$2 JCN Delay_start = true, due to Wildfire startup order
# 30-Jan-03  J-03-41  $$3 JCN Removed ##2, added text_dir

name     ProEText
startup  java
java_app_class  SampleExportPdf
java_app_classpath C:\Users\Hu\workspace\ProE\src\SampleExportPdf.jar;
java_app_start  start
java_app_stop   stop
allow_stop      true
delay_start     false
text_dir        C:\Users\Hu\workspace\ProE\src\text;
end
```


## 全局配置文件 `config.pro`

```
#debug
jlink_java_command C:\Program Files\PTC\Creo Elements\Pro5.0\x86e_win64\obj\JRE\bin\java.exe  -Xdebug -Xnoagent -Xrunjdwp:transport=dt_socket,address=8000,server=y,suspend=y


#undug
jlink_java_command C:\Program Files\PTC\Creo Elements\Pro5.0\x86e_win64\obj\JRE\bin\java.exe 
search_path C:\Users\Hu\Desktop  #if file directory isn't default directory, this is very import, almost cost three day.
```

开发环境下最好修改 {{install_path}}/text 下的config.pro 以及将protk.dat放入这个目录.


## 代码


```

import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;

import com.ptc.cipjava.jxthrowable;
import com.ptc.pfc.pfcArgument.pfcArgument;
import com.ptc.pfc.pfcDrawing.Drawing;
import com.ptc.pfc.pfcExport.PDFExportInstructions;
import com.ptc.pfc.pfcExport.PDFExportMode;
import com.ptc.pfc.pfcExport.PDFOption;
import com.ptc.pfc.pfcExport.PDFOptionType;
import com.ptc.pfc.pfcExport.PDFOptions;
import com.ptc.pfc.pfcExport.pfcExport;
import com.ptc.pfc.pfcGlobal.pfcGlobal;
import com.ptc.pfc.pfcModel.Model;
import com.ptc.pfc.pfcModel.ModelDescriptor;
import com.ptc.pfc.pfcModel.ModelType;
import com.ptc.pfc.pfcModel.Models;
import com.ptc.pfc.pfcModel.pfcModel;
import com.ptc.pfc.pfcSession.RetrieveModelOptions;
import com.ptc.pfc.pfcSession.Session;
import com.ptc.pfc.pfcSession.pfcSession;


public class SampleExportPdf {

	public static void start() throws IOException, jxthrowable {
		// TODO Auto-generated method stub
		
		Session curSession;
		
		String filePath = "C:\\Users\\Hu\\Desktop\\java.log";
 
		// Set the second parameter of FileWriter to "true" to append to file.
		Writer fileWriter = new FileWriter(filePath, true);
		Drawing draw = null;
		PDFExportInstructions pdf_export = null;
		String modelLocation="C:\\Users\\Hu\\Desktop";
		String drw_name = "prt0001.prt";
		// prt0001.prt
		// Asm0001.drw
		
		
		try {
			curSession = pfcGlobal.GetProESession();
			pdf_export = pfcExport.PDFExportInstructions_Create();
			
			PDFOption pdf_option = pfcExport.PDFOption_Create();
			pdf_option.SetOptionType(PDFOptionType.PDFOPT_LAUNCH_VIEWER);
			pdf_option.SetOptionValue(pfcArgument.CreateBoolArgValue(false));
			
			
			PDFOption pdf_option_3d = pfcExport.PDFOption_Create();
			pdf_option_3d.SetOptionType(PDFOptionType.PDFOPT_EXPORT_MODE);
            ## if export prt file to pdf, must add this option, else comment it.
			pdf_option_3d.SetOptionValue(pfcArgument.CreateIntArgValue(PDFExportMode._PDF_3D_AS_U3D_PDF));
			PDFOptions pdf_options = PDFOptions.create();
			pdf_options.append(pdf_option);
			pdf_options.append(pdf_option_3d);
			pdf_export.SetOptions(pdf_options);
			//Load Drawing Files....
			
			ModelDescriptor desc1 = pfcModel.ModelDescriptor_Create(ModelType.MDL_PART, drw_name, null);
			desc1.SetPath (modelLocation);
			fileWriter.write("filename \r\n");
			fileWriter.write(desc1.GetFullName());
			fileWriter.write("\r\n filename \r\n");
			Model model = curSession.RetrieveModel(desc1);
			fileWriter.write("model has been get\r\n");
			model.Display();
			model.Export("prtprtprt", pdf_export);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			fileWriter.write(e.toString());
			
		} finally {
			fileWriter.close();	
		}
		

	}
	
	public static void stop() {
		System.out.println ("------------------end------------------");
	}

}


```



现在drw以及可以，但是prt不行，原因是prt是3d的。  所以PDFOPT_EXPORT_MODE必须设置为PDF_3D_AS_U3D_PDF，才能导出成pdf。

