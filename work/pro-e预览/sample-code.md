import com.ptc.cipjava.jxthrowable;
import com.ptc.pfc.pfcArgument.pfcArgument;
import com.ptc.pfc.pfcDrawing.Drawing;
import com.ptc.pfc.pfcExport.PDFExportInstructions;
import com.ptc.pfc.pfcExport.PDFOption;
import com.ptc.pfc.pfcExport.PDFOptionType;
import com.ptc.pfc.pfcExport.PDFOptions;
import com.ptc.pfc.pfcExport.pfcExport;
import com.ptc.pfc.pfcGlobal.pfcGlobal;
import com.ptc.pfc.pfcModel.ModelDescriptor;
import com.ptc.pfc.pfcModel.ModelType;
import com.ptc.pfc.pfcModel.Models;
import com.ptc.pfc.pfcModel.pfcModel;
import com.ptc.pfc.pfcSession.Session;
import com.ptc.pfc.pfcSession.pfcSession;


public class zmText {
	public static void main(String[] args){
		try {
			proe_start();
		} catch (jxthrowable e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public static void proe_start() throws jxthrowable  {
		// TODO Auto-generated method stub
		
		Session curSession = pfcGlobal.GetProESession();
		
		PDFExportInstructions pdf_export = pfcExport.PDFExportInstructions_Create();
		
		PDFOption pdf_option = pfcExport.PDFOption_Create();
		pdf_option.SetOptionType(PDFOptionType.PDFOPT_LAUNCH_VIEWER);
		pdf_option.SetOptionValue(pfcArgument.CreateBoolArgValue(false));
		PDFOptions pdf_options = PDFOptions.create();
		pdf_options.append(pdf_option);
		pdf_export.SetOptions(pdf_options);
		//Load Drawing Files....

		String modelLocation="\\";
		String drw_name = "C:\\Users\\Hu\\Desktop\\Asm0001.drw";
		ModelDescriptor desc1 = pfcModel.ModelDescriptor_Create(ModelType.MDL_DRAWING, drw_name, null);
		desc1 = pfcModel.ModelDescriptor_CreateFromFileName(drw_name);
		desc1.SetPath (modelLocation);
		Drawing draw=(Drawing)curSession.RetrieveModelWithOpts(desc1, pfcSession.RetrieveModelOptions_Create());
		draw.Display();
		draw.Export(""+draw.GetFullName()+"", pdf_export);
		
		
		
	//Models pdf_models = Models.create();
	//String modelLocation="\\";
	//String drw_name = "text.drw";
	//ModelDescriptor desc1 = pfcModel.ModelDescriptor_Create(ModelType.MDL_DRAWING, drw_name, null);
	//desc1 = pfcModel.ModelDescriptor_CreateFromFileName(drw_name);
	//desc1.SetPath (modelLocation);
	//Drawing draw=(Drawing)curSession.RetrieveModelWithOpts(desc1, pfcSession.RetrieveModelOptions_Create());
	////Get total number of Sheets..
	//int nooffiles=draw.GetNumberOfSheets();
	//for(int no=1;no<=nooffiles;no++)
	// {
	//  draw.SetCurrentSheetNumber(no);
	//  draw.Display();
	// draw.Export(""+draw.GetFullName()+"-"+no+"", pdf_export);
	//continue;
	//}
	////draw.Export(draw.GetFullName(), pdf_export);
	}
	
	public static void proe_stop() {
	
	}

}
