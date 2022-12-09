from odoo import http
from odoo.http import request
import smtplib 
import random


class EmailOtpVarify(http.Controller):

    def __init__ (self):

        self.Otp = Otp = random.randint(1111,9999)
    

    def SendEmail(self,recEmailId,otp="8895"):
            
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("", "")
        message = f"Your One Time Password Is {otp} Donot Share With Any One."
        s.sendmail("tapare.shreyash20@gmail.com", recEmailId, message)
        s.quit()        
    
        

    @http.route('/email/validation', auth='public', website= True)
    def emailValidation(self,**data):

        
        
        if data and request.httprequest.method == 'POST':

            
            self.SendEmail(data["Email"], self.Otp)
            request.session['otp'] =self.Otp
            

        return request.render('vadactro_services.emailValidation')
  
    
    @http.route('/otp/verification', auth='public', website= True)
    def otpVerification(self,**data):

        if str (data["OTP"]) == str(request.session['otp']) :
            
            request.session['otp'] =""
            return request.redirect('/my/home')


        else:

            return request.redirect('/my/account')

 

        return None
       
