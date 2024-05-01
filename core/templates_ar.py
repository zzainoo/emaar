from .models import *
from comps.models import *


def get_section(short_code):
    section = Section.objects.get(short_code=short_code)
    is_background = ""
    if section.is_background:
        is_background = "section-rounded"
    else:
        is_background = ""

    if section.is_reflected:
        data = f'''
            <div class="section-wrapper" >



        	<div class="section {is_background}" data-aos="{section.effect}" data-aos-duration="{section.effect_duration}" >

        		<div >
        			<div class="shape">
        				<img src="{section.image.url}" class="section-image" data-aos="{section.effect}" data-aos-duration="{section.effect_duration + 3000}">
        			</div>
        		</div>
        		<div class="section-text">
        			<p class="title" data-aos="{section.effect}" data-aos-duration="{section.effect_duration}">{section.title}</p>
        			<br>
        			<p class="desc" data-aos="{section.effect}" data-aos-duration="{section.effect_duration + 1000}">{section.desc}</p>
        		</div>
        	</div>


         <a href="{section.button_link}"><div class="action-button3 animate__animated animate__headShake " data-aos="{section.effect}" data-aos-duration="{section.effect_duration + 1000}">
        		<div>
        			{section.button_text}
        		</div>
        	</div></a>

        </div>

            '''
    else:

        data = f'''
        <div class="section-wrapper" >
        <div class="section {is_background}" data-aos="{section.effect}" data-aos-duration="{section.effect_duration}">
            <div class="section-text">
                <p class="title" data-aos="{section.effect}" data-aos-duration="{section.effect_duration}">{section.title}</p>
                <br>
                <p class="desc" data-aos="{section.effect}" data-aos-duration="{section.effect_duration + 1000}">{section.desc}</p>
            </div>
            <div >
                <div class="shape" >
                    <img src="{section.image.url}" class="section-image"data-aos="{section.effect}" data-aos-duration="{section.effect_duration + 3000}" >
                </div>
            </div>
        </div>


        <a href="{section.button_link}"><div class="action-button2 animate__animated animate__headShake ">
            <div>
                {section.button_text}
            </div>
            
        </div></a>
    </div>

        '''

    return data


def get_header(short_code, page):
    header = Header.objects.get(short_code=short_code)
    data = ""
    data += '''
    	<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
  '''
    menu = Menu.objects.get(id=header.menu_id)
    for item in MenuItem.objects.all().filter(menu=menu):
        if item.external is False:
            if item.link.link == '/':
                link = "/"
            else:
                link = f"/{item.link.link}"
        else:
            link = item.link

        if page == item.link.link:
            data += f'''
                       <a href='{link}' class="active">{item.name}</a>
                        '''
        else:

            data += f'''
                  <a href='{link}'>{item.name}</a>
            '''

    data += f'''
    </div>
    <div class="header-wrapper">
	<div class="header" >

		<div class="logo">
			<img src="{header.logo.url}" style="margin:10px;">
		</div>
		<div class="header-menu">
			<div>
				<ul class="umenu-item-list">
				<li class="umenu-item"><i class="fa-solid fa-envelope"></i>{header.email}</li>
					<li class="umenu-item"><i class="fa-solid fa-phone"></i>{header.phone}</li>
					<li class="umenu-item"><i class="fa-solid fa-calendar-days"></i>{header.work_time}</li>

				</ul>
			</div>
			<div>
				<ul class="lmenu-item-list">
    '''

    for item in MenuItem.objects.all().filter(menu=menu):
        if item.external is False:
            if item.link.link == '/':
                link = "/"
            else:
                link = f"/{item.link.link}"
        else:
            link = item.link
        if page == item.link.link:
            data += f'''
                              <li class="lmenu-item item-active"><a href="{item.link.link}">{item.name}</a></li>
                        '''
        else:

            data += f'''
                  <li class="lmenu-item"><a href="{link}">{item.name}</a></li>
            '''

    data += '''
    </ul>
			</div>
		</div>
	</div>

			<div class="hr">

			</div>
    '''

    if header.is_button:
        data += f'''
        <div class="action-button header-btn aheader animate__animated animate__headShake ">
		<a href="{header.button_link}"><div>
			{header.button_text}
		</div></a>
	</div>

       '''
    data += f'''

    <div class="action-button header-btn2 aheader animate__animated animate__headShake " onclick="openNav()">
		<div style="font-size: 30px;">
			&#9776;
		</div>
	</div>
</div>
    '''

    return data


def get_spacer(short_code):
    spacer = Spacer.objects.get(short_code=short_code)
    space = Spacer.objects.get(height=spacer)

    data = f'''
    <div  style="height: {space.height}px;background-color: var(--red);background-image: url(./static/assets/pattern_bg.png);" data-aos="{space.effect}" data-aos-duration="{space.effect_duration}"></div>

    '''

    return data


def get_counter(short_code):
    counter = Counter.objects.get(short_code=short_code)
    data = f'''
     <div class="section2-wrapper">
	<div class="section2">
		<div class="c1" data-aos="fade-up" data-aos-duration="{counter.effect_duration}"><p>{counter.title1}</p><p>{counter.number1}</p></div>
		<div class="c1" data-aos="fade-down" data-aos-duration="{counter.effect_duration}"><p>{counter.title2}</p><p>{counter.number2}</p></div>
		<div class="c1" data-aos="fade-up" data-aos-duration="{counter.effect_duration}"><p>{counter.title3}</p><p>{counter.number3}</p></div>
		<div class="c1" data-aos="fade-down" data-aos-duration="{counter.effect_duration}"><p>{counter.title4}</p><p>{counter.number4}</p></div>
	</div>
</div>
    '''
    return data


def get_masonry(short_code):
    masonry = Masonry.objects.get(short_code=short_code)
    data = f'''
    <div class="section-wrapper">
	<div class="section4" data-aos="{masonry.effect}" data-aos-duration="{masonry.effect_duration}"> 

		<div class="card-wrapper">
			<div class="section-title animate__animated animate__pulse animate__infinite">{masonry.title}</div>
			<div class="card">
				<div class="card-image" style="background: url({masonry.image1.url});background-size:cover;background-repeat:no-repeat;background-position: 50% 50%;"></div>
				<div class="card-icon ficon">{masonry.icon1}</div>
				<div class="card-text">
					<br>
					<br>
					<p class="card-title">{masonry.title1}</p>
					<p class="card-desc">{masonry.description1}.</p>
					<br>
				</div>
			</div>
		</div>



				<div class="card-wrapper" >
			<div class="card"> 
				<div class="card-image" style="background-image: url({masonry.image2.url});background-size:cover;background-repeat:no-repeat;background-position: 50% 50%;"></div>
				<div class="card-icon"><i class="fa-solid fa-envelope" style="color:white;"></i></div>
				<div class="card-text">
					<br>
					<br>
					<p class="card-title">{masonry.title2}</p>
					<p class="card-desc">{masonry.description2}.</p>
					<br>
				</div>
			</div>
		</div>





		<div class="card-wrapper section4last">
			<div class="card">
				<div class="card-image" style="background-image: url({masonry.image3.url});background-size:cover;background-repeat:no-repeat;background-position: 50% 50%;" ></div>
				<div class="card-icon"><i class="fa-solid fa-envelope" style="color:white;"></i></div>
				<div class="card-text">
					<br>
					<br>
					<p class="card-title">{masonry.title3}</p>
					<p class="card-desc">{masonry.description3}.</p>
					<br>
				</div>
			</div>
		</div>

	</div>
</div>
    '''
    return data


def get_blog(short_code):
    blog = BlogComp.objects.get(short_code=short_code)
    if blog.is_simple:
        data = f'''
        <div class="section-wrapper" >
        <div class="section3" data-aos="{blog.effect}" data-aos-duration="{blog.effect_duration}">
            <div>
                {blog.title}
            </div>

            <div class="posts">
        '''
        for post in Post.objects.all().filter(category=blog.category)[0:4]:
            link = f"/posts/{post.pk}"

            data += f'''
                            <div class="post-wrapper">
                        <div class="post">
                            <div class="post-image" style="background-image: url({post.image.url});background-size:contain;background-repeat:no-repeat;background-position: 50% 50%;"></div>
                            <div class="post-text">
                                <p class="post-title">{post.name}</p>
                                <p class="post-desc">{post.desc} ،</p>
                                <br>
                            </div>
                        </div>
                           <a href="{link}" class="post-btn"> <div>المزيد</div></a>
                </div>
            '''

        data += f'''
        </div>


        <a href="{blog.button_link}"><div class="action-button center-button animate__animated animate__headShake ">
            <div>
                {blog.button_text}
            </div>
        </div></a>

        </div>



    </div>

        '''
    else:
        data = f'''

            <div class="section6" data-aos="{blog.effect}" data-aos-duration="{blog.effect_duration}">
            '''
        for post in Post.objects.all().filter(category=blog.category)[0:blog.count]:
            link = f"/posts/{post.pk}"

            data += f'''
                                <div class="post-wrapper">
                            <div class="post">
                                <div class="post-image" style="background-image: url({post.image.url});background-size:contain;background-repeat:no-repeat;background-position: 50% 50%;"></div>
                                <div class="post-text">
                                    <p class="post-title">{post.name}</p>
                                    <p class="post-desc">{post.desc} ،</p>
                                    <br>
                                </div>
                            </div>
                           <a href="{link}" class="post-btn"> <div>المزيد</div></a>
                    </div>
                '''
        data += f'''
        </div>
            '''

    return data


def get_project(short_code):
    blog = ProjectComp.objects.get(short_code=short_code)

    if blog.is_simple:
        data = f'''
        <div class="section-wrapper" >
        <div class="section3" data-aos="{blog.effect}" data-aos-duration="{blog.effect_duration}">
            <div >
                {blog.title}
            </div>

            <div data-aos-duration="1000" class="posts">
        '''
        for post in Project.objects.all().filter(category=blog.category)[0:4]:
            link = f"/projects/{post.pk}"
            data += f'''
                            <div class="post-wrapper">
                        <div class="post">
                            <div class="post-image" style="background-image: url({post.image.url});background-size:contain;background-repeat:no-repeat;background-position: 50% 50%;"></div>
                            <div class="post-text">
                                <p class="post-title">{post.name}</p>
                                <p class="post-desc">{post.desc} ،</p>
                                <br>
                            </div>
                        </div>
                           <a href="{link}" class="post-btn"> <div>المزيد</div></a>
                </div>
            '''

        data += f'''
        </div>


        <a href="{blog.button_link}"><div class="action-button2 center-button animate__animated animate__headShake ">
            <div>
                {blog.button_text}
            </div>
        </div></a>

        </div>



    </div>

        '''
    else:
        data = f'''
            <div class="section6" data-aos="{blog.effect}" data-aos-duration="{blog.effect_duration}">
            '''
        for post in Project.objects.all().filter(category=blog.category)[0:blog.count]:
            link = f"/projects/{post.pk}"
            data += f'''
                                <div class="post-wrapper">
                            <div class="post">
                                <div class="post-image" style="background-image: url({post.image.url});background-size:contain;background-repeat:no-repeat;background-position: 50% 50%;"></div>
                                <div class="post-text">
                                    <p class="post-title">{post.name}</p>
                                    <p class="post-desc">{post.desc} ،</p>
                                    <br>
                                </div>
                            </div>
                           <a href="{link}" class="post-btn"> <div>المزيد</div></a>
                    </div>
                '''
        data += f'''
        </div>
            '''

    return data


def get_footer(short_code):
    footer = Footer.objects.get(short_code=short_code)
    data = f'''
        <div class="section3 footer" data-aos="{footer.effect}" data-aos-duration="{footer.effect_duration}">

	<div>
		<img src="{footer.logo.url}">
		<br>
		<p class="footer-desc">
			{footer.desc}
		</p>
	</div>
	<div>
<br>
		<p class="footer-menu-title">{footer.title1}</p>
		
		<ul class="footer-menu">
    '''

    for item in MenuItem.objects.all().filter(menu=footer.menu1):
        data += f'''
        <li class="footer-item"><a href="{item.link.link}">{item.name}</a></li>
        '''

    data += f'''
    	</ul>
	</div>

		<div>
		<br>
		<p class="footer-menu-title">{footer.title2}</p>
				<ul class="footer-menu" style="list-style: none;">

            
            <li class="footer-item"><i class="fa-solid fa-envelope"></i> {footer.email}</li>
			<li class="footer-item"><i class="fa-solid fa-phone"></i> {footer.phone}</li>
			<li class="footer-item"><i class="fa-solid fa-calendar-days"></i> {footer.work_time}</li>
           	</ul>
       	</div>

       		

</div>
<div style="text-align:center;padding:5px;" data-aos="{footer.effect}" data-aos-duration="{footer.effect_duration}"> © 1998-2024
. All rights reserved , By Teatro Agency </div>
'''
    return data


def get_contact(short_code):
    contact = Contact.objects.get(short_code=short_code)
    data = f'''
        	<div class="section7" data-aos="{contact.effect}" data-aos-duration="{contact.effect_duration}">
		<div>
			<p>الرجاء ملئ جميع الحقول</p>
				<br>
								<br>

				<form action="mailto:{contact.dest_email}">
					<input type="text" placeholder="الاسم">


<input type="text" placeholder="البريد الالكتروني">
<input type="text" placeholder="عنوان الرسالة">
						<textarea rows="10">الرسالة
						</textarea>

    <button type="submit">ارسال</button>
				</form>
		</div>




		<div >
						<p >الرجاء ملئ جميع الحقول</p>
				<br>
				<br>

				<h5><i class="fa-solid fa-phone"></i>{contact.phone1}</h5>
					<h5><i class="fa-solid fa-phone"></i>{contact.phone2}</h5>
						<h5><i class="fa-solid fa-envelope"></i>{contact.email}</h5>
							<h5><i class="fa-solid fa-house"></i>{contact.location}</h5>



		</div>



	</div>
    '''
    return data
