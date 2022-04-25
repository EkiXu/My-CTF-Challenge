<?php
namespace app\controller;

use app\BaseController;

use Dompdf\Dompdf;


class Printer extends BaseController
{
    public function print(): \think\response\File
    {   
        $page = $this->request->param("page");

        $html = file_get_contents("http://localhost:81/".$page);
        
        $filename = "export.pdf";
    
        $dompdf = new Dompdf();
        $dompdf->loadHtml($html);
        $dompdf->setPaper('A5', 'portrait');
    
        // lets us know if something goes wrong
        global $_dompdf_show_warnings;
        $_dompdf_show_warnings = true;
    
        // render the HTML as PDF
        $dompdf->render();
    
        // output the generated PDF to browser
        return download($dompdf->output(), $filename, true);
    }
}