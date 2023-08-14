#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import smtplib
import mimetypes
from string import Template
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage

# --- Simple Email sender ----

class mail_error(Exception):
    pass

class mail:
    def __init__(self,
                 a_sServer,
                 a_sUser,
                 a_sPassword,
                 a_nPort,
                 a_bStarttls = False,
                 a_sMailAddrFrom = "noreply@example.com"):
        self.sServer = a_sServer
        self.sUser = a_sUser
        self.sPassword = a_sPassword
        self.nPort = a_nPort
        self.bStarttls = a_bStarttls
        self.sMailAddrFrom = a_sMailAddrFrom
        self.SetHtmlBodyFormat()

    def SetHtmlBodyFormatToPreFormattedText(self):
        self.SetHtmlBodyFormat('<html><body><pre>',
                               '</pre></body></html>')

    def SetHtmlBodyFormat(self,
                          a_sHtmlBodyStart = '<html><body>',
                          a_sHtmlBodyEnd   = '</body></html>'):
        self.sHtmlBodyStart = a_sHtmlBodyStart
        self.sHtmlBodyEnd = a_sHtmlBodyEnd

    def formatmessage(self,
                      a_sMailAddrTo,
                      a_sMsg,
                      a_sSubject,
                      a_tFileAttachments,
                      a_bEmbedImages = False):
        # Main message
        message = MIMEMultipart("mixed")
        message["Subject"] = a_sSubject
        message["From"] = self.sMailAddrFrom
        message["To"] = a_sMailAddrTo

        # Message body
        message_body = MIMEMultipart("alternative")
        message_body.attach(MIMEText(a_sMsg, "plain"))
        message_body.attach(MIMEText(f'{self.sHtmlBodyStart}{a_sMsg}{self.sHtmlBodyEnd}', "html"))
        message.attach(message_body)

        # File attachments
        for f in a_tFileAttachments:
            #file_path = os.path.join(dir_path, f)
            try:
                type, enc = mimetypes.guess_type(f)
                if a_bEmbedImages and "image/" in type:
                    attachment = MIMEImage(open(f, "rb").read())
                    attachment.add_header('Content-ID',f'<{os.path.basename(f)}>') ## shorten filename, do not use full path
                    attachment.add_header('Content-Disposition','attachment', filename=os.path.basename(f)) ## shorten filename, do not use full path
                else:
                    attachment = MIMEApplication(open(f, "rb").read(), _subtype = 'octet-stream')
                    attachment.add_header('Content-Disposition','attachment', filename=os.path.basename(f)) ## shorten filename, do not use full path
                # Attach to main message
                message.attach(attachment)
            except OSError as e:
                raise mail_error(f'Could not attach file {f}: {str(e)}')

        #return message.as_string()
        return message

    def send_template(self,
                      a_sMailAddrTo,
                      a_sMsgTemplateFile,
                      a_tMsgTemplateDict,
                      a_sSubject,
                      a_tFileAttachments = list(),
                      a_bEmbedImages = False):
        try:
            with open(a_sMsgTemplateFile, 'r') as f:
                tpl = Template(f.read())
                msg = tpl.safe_substitute(a_tMsgTemplateDict)
                self.send(a_sMailAddrTo, msg, a_sSubject, a_tFileAttachments, a_bEmbedImages)
        except OSError as e:
               raise mail_error(f'Could not read template file {a_sMsgTemplateFile}: {str(e)}')

    def send(self,
             a_sMailAddrTo,
             a_sMsg,
             a_sSubject,
             a_tFileAttachments = list(),
             a_bEmbedImages = False):
        try:
            if self.bStarttls:
                with smtplib.SMTP(host = self.sServer, port = self.nPort) as mailer:
                    mailer.starttls()
                    mailer.login(user = self.sUser, password = self.sPassword)
                    mailer.send_message(from_addr = self.sMailAddrFrom,
                                        to_addrs = a_sMailAddrTo,
                                        msg = self.formatmessage(a_sMailAddrTo,
                                                                 a_sMsg,
                                                                 a_sSubject,
                                                                 a_tFileAttachments,
                                                                 a_bEmbedImages))
            else:
                with smtplib.SMTP_SSL(host = self.sServer, port = self.nPort) as mailer:
                    mailer.login(user = self.sUser, password = self.sPassword)
                    mailer.send_message(from_addr = self.sMailAddrFrom,
                                        to_addrs = a_sMailAddrTo,
                                        msg = self.formatmessage(a_sMailAddrTo,
                                                                 a_sMsg,
                                                                 a_sSubject,
                                                                 a_tFileAttachments,
                                                                 a_bEmbedImages))
        except Exception as e:
            raise
