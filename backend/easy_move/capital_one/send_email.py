# coding=utf-8
import boto3
import os
import json
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
client = boto3.client('ses',
    region_name='us-east-1',
    aws_access_key_id='AKIAJYUPLUUN4CIHQL6Q',
    aws_secret_access_key='fHFwcMuQHZyjVMeY9paxR6QGlLBQvn2QpbEDt+e9'
)
def email(bodytext = 'No data...check your function arguments', toAddress= 'dayumikoda@gmail.com', subject='Notification to close electricity account from Easy Move', dftoconvert = None, replace=False):
    region = 'us-east-1'
    me = 'support@zoesh.com'
    destination = { 'ToAddresses' : [toAddress,'kennethcc2005@gmail.com'],
                    'CcAddresses' : [],
                    'BccAddresses' : []}
    mail_sender = 'support@zoesh.com'
    mail_receivers_list  = ['kennethcc2005@gmail.com'
        ]
    # mail_subject = 'test'
    mail_subject = 'Notification to close electricity account from Easy Move'
    mail_content = email_body()
    message_dict = { 'Data':
      'From: ' + mail_sender + '\n' + 'To: ' + str(mail_receivers_list) + '\n'+ 'Subject: ' + mail_subject + '\n'+ 'MIME-Version: 1.0\n'+'Content-Type: text/html;\n\n' +mail_content} 

    try:
        bodyhtml = dftoconvert.to_html(float_format = lambda x: '({:15,.2f})'.format(abs(x)) if x < 0 else '+{:15,.2f}+'.format(abs(x)))
        # use no-break space instead of two spaces next to each other
        if replace:
            bodyhtml = bodyhtml.replace('  ', '&nbsp;')
        message = {'Subject' : {'Data' : subject},
                   'Body': {'Html' : {'Data' : bodyhtml}}}
    except: #If there is no data to convert to html
        bodytext =mail_content
        message = {'Subject' : {'Data' : subject},
                   'Body': {'Html' : {'Data' : bodytext}}}
        print 'here'
    result = client.send_email(Source = me, 
                               Destination = destination, 
                               Message = message)   
    
    print len(mail_content), type(mail_content), 
    return result if 'ErrorResponse' in result else True

def html_decode(s):
    """
    Returns the ASCII decoded version of the given HTML string. This does
    NOT remove normal HTML tags like <p>.
    """
    htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;')
        )
    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s

def email_body():
    html = '''
    <!doctype html>
<html>
<head>
<title></title>
<style type="text/css">
/* CLIENT-SPECIFIC STYLES */
body, table, td, a { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }
table, td { mso-table-lspace: 0pt; mso-table-rspace: 0pt; }
img { -ms-interpolation-mode: bicubic; }

/* RESET STYLES */
img { border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none; }
table { border-collapse: collapse !important; }
body { height: 100% !important; margin: 0 !important; padding: 0 !important; width: 100% !important; }

/* iOS BLUE LINKS */
a[x-apple-data-detectors] {
    color: inherit !important;
    text-decoration: none !important;
    font-size: inherit !important;
    font-family: inherit !important;
    font-weight: inherit !important;
    line-height: inherit !important;
}

/* MOBILE STYLES */
@media screen and (max-width: 600px) {
  .img-max {
    width: 100% !important;
    max-width: 100% !important;
    height: auto !important;
  }

  .max-width {
    max-width: 100% !important;
  }

  .mobile-wrapper {
    width: 85% !important;
    max-width: 85% !important;
  }

  .mobile-padding {
    padding-left: 5% !important;
    padding-right: 5% !important;
  }
}

/* ANDROID CENTER FIX */
div[style*="margin: 16px 0;"] { margin: 0 !important; }
</style>
</head>
<body style="margin: 0 !important; padding: 0; !important background-color: #ffffff;" bgcolor="#ffffff">

<!-- HIDDEN PREHEADER TEXT -->
<div style="display: none; font-size: 1px; color: #fefefe; line-height: 1px; font-family: Open Sans, Helvetica, Arial, sans-serif; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;">
    Lorem ipsum dolor que ist
</div>

<table border="0" cellpadding="0" cellspacing="0" width="100%">
    <tr>
        <td align="center" valign="top" width="100%" background="bg.jpg" bgcolor="#3b4a69" style="background: #3b4a69 url('bg.jpg'); background-size: cover; padding: 50px 15px;" class="mobile-padding">
            <!--[if (gte mso 9)|(IE)]>
            <table align="center" border="0" cellspacing="0" cellpadding="0" width="600">
            <tr>
            <td align="center" valign="top" width="600">
            <![endif]-->
            <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;">
                <tr>
                    <td align="center" valign="top" style="padding: 0; font-family: Open Sans, Helvetica, Arial, sans-serif;">
                        <h1 style="font-size: 40px; color: #ffffff;">Account Closure Requests</h1>
                        <p style="color: #ffffff; font-size: 20px; line-height: 28px; margin: 0;">
                          Move out address: 15 KIMBERLY LN, MORRISONVILLE, NY
                        </p>
                    </td>
                </tr>
            </table>
            <!--[if (gte mso 9)|(IE)]>
            </td>
            </tr>
            </table>
            <![endif]-->
        </td>
    </tr>
    <tr>
        <td align="center" height="100%" valign="top" width="100%" bgcolor="#f6f6f6" style="padding: 50px 15px;" class="mobile-padding">
            <!--[if (gte mso 9)|(IE)]>
            <table align="center" border="0" cellspacing="0" cellpadding="0" width="600">
            <tr>
            <td align="center" valign="top" width="600">
            <![endif]-->
            <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;">
                <tr>
                    <td align="center" valign="top" style="padding: 0 0 25px 0; font-family: Open Sans, Helvetica, Arial, sans-serif;">
                        <table cellspacing="0" cellpadding="0" border="0" width="100%">
                          
                            <tr>
                                <td align="center" bgcolor="#ffffff" style="border-radius: 0 0 3px 3px; padding: 25px;">
                                    <table cellspacing="0" cellpadding="0" border="0" width="100%">
                                        <tr>
                                            <td align="center" style="font-family: Open Sans, Helvetica, Arial, sans-serif;">
                                                <table align="center" border="0" cellpadding="0" cellspacing="0" width="80%" style="max-width: 200px;">
                                                    <tr>
                                                        <td align="center" bgcolor="red" style="color: #ffffff; font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 14px; padding: 10px; border-radius: 3px 3px 0 0;">
                                                            Move Out Date
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td align="center" bgcolor="#ffffff" style="color: #444444; font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 24px; padding: 15px; border-radius: 0 0 3px 3px;">
                                                            Oct. 31, 2017
                                                        </td>
                                                    </tr>
                                                </table>
                                                <p style="color: #999999; font-size: 16px; line-height: 24px; margin: 0;">
                                                  We are working on closing the following accounts as requested
                                                </p>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td align="center">
                                                <tr><td>
                                                    <img src="https://ci3.googleusercontent.com/proxy/IQahZVq8RnsGGUT5P_dRhdAKB7Uk49NXr5pmKfCiQZDLTeGDLVz8CBjmzVwdqY8T6OJ_1IQ1aL7-HPiuJB_GOXXdRc1sK1cr9RnLJGGv26jp7VvAw_-j5ZMQ-NyMxNkXAOi6Rg=s0-d-e1-ft#https://cdn.evbstatic.com/s3-s3/marketing/emails/modules/ridges_top_fullx2.jpg" alt="eventbrite" height="7" style="height:7px;border:none;display:block" border="0" class="CToWUd">
                                                </td></tr>
                                              <tr><td class="m_7074652305611002464grid__col" style="font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif;padding:32px 40px;background-color:#ededed">
        <table cellpadding="0" cellspacing="0" border="0" style="width:100%;margin-bottom:12px" class="m_7074652305611002464no_text_resize">
            <tbody><tr>
                <td style="border-bottom:1px dashed #d3d3d3">
                    

<h2 style="color:#404040;font-weight:300;margin:0 0 12px 0;font-size:24px;line-height:30px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif">

                        Request Details
                    
</h2>

                </td>
                <td colspan="2" style="text-align:right;border-bottom:1px dashed #d3d3d3">
                    

<div style="color:#666666;font-weight:400;font-size:13px;line-height:18px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif">
    
                        Oct. 22, 2017
                    
</div>

                </td>
            </tr>
            <tr>
                <td colspan="3">
                    

<p style="color:#666666;font-weight:400;font-size:15px;line-height:21px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif;margin-bottom:18px">
    
                        Ref #: 659752786
                    
</p>

                    <table cellpadding="0" cellspacing="0" border="0" style="width:100%">
                        <thead>
                            <tr>
        
                                <th style="border-bottom:1px dashed #d3d3d3;text-align:left;padding-bottom:12px;padding-right:12px">
                                    
    

<div style="color:#666666;font-weight:400;font-size:15px;line-height:21px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif;font-weight:500">
    
    
                                        Account ID
                                    
    
</div>


                                </th>
                                <th style="border-bottom:1px dashed #d3d3d3;text-align:left;padding-bottom:12px;padding-right:12px">
                                    
    

<div style="color:#666666;font-weight:400;font-size:15px;line-height:21px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif;font-weight:500">
    
    
                                        Company Name
                                    
    
</div>


                                </th>
                                <th style="border-bottom:1px dashed #d3d3d3;text-align:left;padding-bottom:12px;padding-right:12px">
                                    
    

<div style="color:#666666;font-weight:400;font-size:15px;line-height:21px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif;font-weight:500">
    
    
                                        Type
                                    
    
</div>


                                </th>
                                <th style="border-bottom:1px dashed #d3d3d3;text-align:right;padding-bottom:12px;padding-right:0">
                                    
    

<div style="color:#666666;font-weight:400;font-size:15px;line-height:21px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif;font-weight:500">
    
    
                                        Status
                                    
    
</div>


                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                
                                <td style="padding:12px 0;padding-right:3px">
                                    

<div style="color:#666666;font-weight:400;font-size:15px;line-height:21px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif">
    
                                        16816888
                                    
</div>

                                </td>
                                
                                <td style="padding:12px 0;padding-right:3px">
                                    

<div style="color:#666666;font-weight:400;font-size:15px;line-height:21px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif">
    
                                        PG&E
                                    
</div>

                                </td>
                                
                                <td style="padding:12px 0;padding-right:3px">
                                    

<div style="color:#666666;font-weight:400;font-size:15px;line-height:21px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif">
    
                                        Electric Utility 
                                    
</div>

                                </td>
                                
                                <td style="text-align:right;padding:12px 0">
                                    

<div style="color:#666666;font-weight:400;font-size:15px;line-height:21px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif">
    
                                        In Progress
                                    
</div>

                                </td>
                            </tr>
                            <tr>
                                
                                <td style="padding:12px 0;padding-right:3px">
                                    

<div style="color:#666666;font-weight:400;font-size:15px;line-height:21px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif">
    
                                        <span class="il">233233233</span>
                                    
</div>

                                </td>
                                
                                <td style="padding:12px 0;padding-right:3px">
                                    

<div style="color:#666666;font-weight:400;font-size:15px;line-height:21px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif">
    
                                        Xfinity
                                    
</div>

                                </td>
                                
                                <td style="padding:12px 0;padding-right:3px">
                                    

<div style="color:#666666;font-weight:400;font-size:15px;line-height:21px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif">
    
                                        Internet
                                    
</div>

                                </td>
                                
                                <td style="text-align:right;padding:12px 0">
                                    

<div style="color:#666666;font-weight:400;font-size:15px;line-height:21px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif">
    
                                       In Progress
                                    
</div>

                                </td>
                            </tr>
                            <tr>
                                
                                <td style="padding:12px 0;padding-right:3px">
                                    

<div style="color:#666666;font-weight:400;font-size:15px;line-height:21px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif">
    
                                       10012345
                                    
</div>

                                </td>
                                
                                <td style="padding:12px 0;padding-right:3px">
                                    

<div style="color:#666666;font-weight:400;font-size:15px;line-height:21px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif">
    
                                        RECOLOGY
                                    
</div>

                                </td>
                                
                                <td style="padding:12px 0;padding-right:3px">
                                    

<div style="color:#666666;font-weight:400;font-size:15px;line-height:21px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif">
    
                                        Waster Collection
                                    
</div>

                                </td>
                                
                                <td style="text-align:right;padding:12px 0">
                                    

<div style="color:#666666;font-weight:400;font-size:15px;line-height:21px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif">
    
                                        In Progress
                                    
</div>

                                </td>
                            </tr>
                            
                        </tbody>
                    </table>
                </td>
            </tr>
            <tr>
                <td></td>
                
              
            </tr>
        </tbody></table>
        
        
    
    
   


    


    </td></tr>
                                              <tr><td class="m_-917084520158219420table__ridge m_-917084520158219420table__ridge--bottom">
    <img src="https://ci6.googleusercontent.com/proxy/ChkWB3VCDXts8fGD_fBmRzOcAG5oJwt9sGbDs6uysurO_fiBa2BV4lrAGSNt9MvTKvqx5M4v_WcCBRHhQd8y-tQIsA_1t6ZnpR8YDXy3o1GWtyEeazTP0MixLEvW1SaAohvp3R7p3Q=s0-d-e1-ft#https://cdn.evbstatic.com/s3-s3/marketing/emails/modules/ridges_bottom_fullx2.jpg" alt="eventbrite" height="7" style="height:7px;border:none;display:block" border="0" class="CToWUd">
</td></tr>
                                              <tr>
        <td class="m_-917084520158219420grid__col" style="font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif;padding:32px 40px;border-radius:0 0 6px 6px" align="">
            
    
    
<table cellpadding="0" cellspacing="0" border="0" align="left" style="width:260px;line-height:1.67;font-size:13px" class="m_-917084520158219420small_full_width">
    <tbody><tr>
        
<h2 style="color:#404040;font-weight:300;margin:0 0 12px 0;font-size:24px;line-height:30px;font-family:'Benton Sans',-apple-system,BlinkMacSystemFont,Roboto,'Helvetica neue',Helvetica,Tahoma,Arial,sans-serif">
Manage your accounts from Easy Move
</h2>

    </tr>
<td align="center" style="border-radius: 26px;" bgcolor="#75b6c9">
                                                            <a href="http://localhost:3000" target="_blank" style="font-size: 16px; font-family: Open Sans, Helvetica, Arial, sans-serif; color: #ffffff; text-decoration: none; border-radius: 26px; background-color: #75b6c9; padding: 14px 26px; border: 1px solid #75b6c9; display: block;">Log in &rarr;</a>
                                                        </td>
</tbody></table>
    '''
    unescaped = html_decode(html)
    print type(unescaped), len(unescaped)
    return unescaped

if __name__ == '__main__':
    email()
