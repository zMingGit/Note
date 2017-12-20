## Requirement

customize background image of login page

## Provide API

can upload iamge to replace background image.


	POST api/v2.1/admin/login-background-image/
	
	Response({'success': True})
	
	400: Bad Request 
	500: Internal Server Error
	


## Interface Change

	System Admin -> Setting:
		Add option, can upload file and submit request.
		Display background image that is currently active.

## Code change

#### admin/login_bg_image.py 
Add varible `CUSTOM_LOGIN_BG_IMAGE_PATH`

```
	control the image saved place.
```
get file, and then create dir if custom dir isn't exists.at last create or replace image file.

#### seahub/auth/views.py ->  login function

If the custom file exists, the custom path is returned, otherwise the file path defined in the setting.py file is returned.

#### seahub/templates/registration/login.html
use the image path varible that auth/views.py->login method returned.