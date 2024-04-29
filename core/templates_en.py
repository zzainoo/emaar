from .models import *
from comps.models import *


def get_section_en(short_code):
    section = Section.objects.get(short_code=short_code)
    is_background = ""
    if section.is_background:
        is_background = "section-rounded"
    else:
        is_background = ""

    if section.is_reflected:
        data = f'''
            <div class="section-wrapper" >



        	<div class="section {is_background}" data-aos="{section.effect}" data-aos-duration="{section.effect_duration}">

        		<div data-aos-duration="1000">
        			<div class="shape animate__animated animate__bounceInLeft">
        				<img src="{section.image_e.url}" class="section-image" >
        			</div>
        		</div>
        		<div>
        			<p class="title">{section.title_e}</p>
        			<br>
        			<p class="desc">{section.desc_e}</p>
        		</div>
        	</div>


       <a href="{section.button_link}"><div class="action-button animate__animated animate__headShake ">
        		<div>
        			{section.button_text_e}
        		</div>
        	</div></a>

        </div>

            '''
    else:

        data = f'''
        <div class="section-wrapper" >
        <div class="section {is_background}" data-aos="{section.effect}" data-aos-duration="{section.effect_duration}">
            <div>
                <p class="title">{section.title_e}</p>
                <br>
                <p class="desc">{section.desc_e}</p>
            </div>
            <div data-aos-duration="1000">
                <div class="shape animate__animated animate__bounceInRight">
                    <img src="{section.image_e.url}" class="section-image" >
                </div>
            </div>
        </div>


         <a href="{section.button_link}"><div class="action-button2 animate__animated animate__headShake ">
           <div>
                {section.button_text_e}
            </div>
            
        </div></a>
    </div>

        '''

    return data


def get_header_en(short_code, page):
    header = Header.objects.get(short_code=short_code)
    data = ""
    data += '''
    	<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
  '''
    menu = Menu.objects.get(id=header.menu_id)
    for item in MenuItem.objects.all().filter(menu=menu):
        if page == item.link.link:
            data += f'''
                       <a href='{item.link.link}' class="active">{item.name_e}</a>
                        '''
        else:

            data += f'''
                  <a href='{item.link.link}'>{item.name_e}</a>
            '''

    data += f'''
    </div>
    <div class="header-wrapper" >
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
        if (item.link.link == '/'):
            link = "/"
        else:
            link = f"/{item.link.link}"
        if page == item.link.link:
            data += f'''
                              <li class="lmenu-item item-active"><a href="{item.link.link}">{item.name_e}</a></li>
                        '''
        else:

            data += f'''
                  <li class="lmenu-item"><a href="{link}">{item.name_e}</a></li>
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
			{header.button_text_e}
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


def get_spacer_en(short_code):
    spacer = Spacer.objects.get(short_code=short_code)
    data = f'''
    <div  style="height: {spacer.height}px;background-color: var(--red);background-image: url(./static/assets/pattern_bg.png);" data-aos="{Spacer.effect}" data-aos-duration="{Spacer.effect_duration}"></div>

    '''

    return data


def get_counter_en(short_code):
    counter = Counter.objects.get(short_code=short_code)
    data = f'''
     <div class="section2-wrapper" data-aos="{counter.effect}" data-aos-duration="{counter.effect_duration}">
	<div class="section2">
		<div class="animate__animated animate__bounceInUp animate__faster"><p>{counter.title1_e}</p><p>{counter.number1}</p></div>
		<div class="animate__animated animate__bounceInUp animate__fast"><p>{counter.title2_e}</p><p>{counter.number2}</p></div>
		<div class="animate__animated animate__bounceInUp "><p>{counter.title3_e}</p><p>{counter.number3}</p></div>
		<div class="animate__animated animate__bounceInUp animate__slow	"><p>{counter.title4_e}</p><p>{counter.number4}</p></div>
	</div>
</div>
    '''
    return data


def get_masonry_en(short_code):
    masonry = Masonry.objects.get(short_code=short_code)
    data = f'''
    <div class="section-wrapper">
	<div class="section4" data-aos="{masonry.effect}" data-aos-duration="{masonry.effect_duration}"> 

		<div class="card-wrapper">
			<div class="section-title animate__animated animate__pulse animate__infinite">{masonry.title_e}</div>
			<div class="card">
				<div class="card-image" style="background: url({masonry.image1.url});background-size:cover;background-repeat:no-repeat;background-position: 50% 50%;"></div>
				<div class="card-icon ficon">{masonry.icon1}</div>
				<div class="card-text">
					<br>
					<br>
					<p class="card-title">{masonry.title1_e}</p>
					<p class="card-desc">{masonry.description1_e}.</p>
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
					<p class="card-title">{masonry.title2_e}</p>
					<p class="card-desc">{masonry.description2_e}.</p>
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
					<p class="card-title">{masonry.title3_e}</p>
					<p class="card-desc">{masonry.description3_e}.</p>
					<br>
				</div>
			</div>
		</div>

	</div>
</div>
    '''
    return data


def get_blog_en(short_code):
    blog = BlogComp.objects.get(short_code=short_code)
    if blog.is_simple:
        data = f'''
        <div class="section-wrapper" >
        <div class="section3" data-aos="{blog.effect}" data-aos-duration="{blog.effect_duration}">
            <div>
                {blog.title_e}
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
                                <p class="post-title">{post.name_e}</p>
                                <p class="post-desc">{post.desc_e} ،</p>
                                <br>
                            </div>
                        </div>
                           <a href="{link}" class="post-btn"> <div>more</div></a>
                </div>
            '''

        data += f'''
        </div>


       <a href="{blog.button_link}"> <div class="action-button center-button animate__animated animate__headShake ">
            <div>
                {blog.button_text_e}
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
                                    <p class="post-title">{post.name_e}</p>
                                    <p class="post-desc">{post.desc_e} ،</p>
                                    <br>
                                </div>
                            </div>
                           <a href="{link}" class="post-btn"> <div>more</div></a>
                    </div>
                '''
        data += f'''
        </div>
            '''

    return data


def get_project_en(short_code):
    blog = ProjectComp.objects.get(short_code=short_code)

    if blog.is_simple:
        data = f'''
        <div class="section-wrapper" >
        <div class="section3" data-aos="{blog.effect}" data-aos-duration="{blog.effect_duration}">
            <div >
                {blog.title_e}
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
                                <p class="post-title">{post.name_e}</p>
                                <p class="post-desc">{post.desc_e} ،</p>
                                <br>
                            </div>
                        </div>
                           <a href="{link}" class="post-btn"> <div>more</div></a>
                </div>
            '''

        data += f'''
        </div>


        <a href="{blog.button_link}"> <div class="action-button2 center-button animate__animated animate__headShake ">
           <div>
                {blog.button_text_e}
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
                                    <p class="post-title">{post.name_e}</p>
                                    <p class="post-desc">{post.desc_e} ،</p>
                                    <br>
                                </div>
                            </div>
                           <a href="{link}" class="post-btn"> <div>more</div></a>
                    </div>
                '''
        data += f'''
        </div>
            '''

    return data


def get_footer_en(short_code):
    footer = Footer.objects.get(short_code=short_code)
    data = f'''
        <div class="section3 footer" data-aos="{footer.effect}" data-aos-duration="{footer.effect_duration}">

	<div>
		<img src="{footer.logo.url}">
		<br>
		<p class="footer-desc">
			{footer.desc_e}
		</p>
	</div>
	<div>
<br>
		<p class="footer-menu-title">{footer.title_e1}</p>
		
		<ul class="footer-menu">
    '''

    for item in MenuItem.objects.all().filter(menu=footer.menu1):
        data += f'''
        <li class="footer-item"><a href="{item.link.link}">{item.name_e}</a></li>
        '''

    data += f'''
    	</ul>
	</div>

		<div>
		<br>
		<p class="footer-menu-title">{footer.title_e2}</p>
				<ul class="footer-menu">


  <li class="footer-item"><i class="fa-solid fa-envelope"></i> {footer.email}</li>
			<li class="footer-item"><i class="fa-solid fa-phone"></i> {footer.phone}</li>
			<li class="footer-item"><i class="fa-solid fa-calendar-days"></i> {footer.work_time}</li>


           	</ul>
       	</div>

    

   

</div>
'''
    return data


def get_contact_en(short_code):
    contact = Contact.objects.get(short_code=short_code)
    data = f'''
        	<div class="section7" data-aos="{contact.effect}" data-aos-duration="{contact.effect_duration}">
		<div>
			<p>please fill the form below</p>
				<br>
								<br>

				<form action="mailto:{contact.dest_email}">
					<input type="text" placeholder="name">


<input type="text" placeholder="email">
<input type="text" placeholder="subject">
						<textarea rows="10">message
						</textarea>


				</form>
		</div>




		<div >
						<p >Additional Information</p>
				<br>
				<br>

				<h5><i class="fa-solid fa-phone"></i>{contact.phone1}</h5>
					<h5><i class="fa-solid fa-phone"></i>{contact.phone2}</h5>
						<h5><i class="fa-solid fa-envelope"></i>{contact.email}</h5>
							<h5><i class="fa-solid fa-house"></i>{contact.location_e}</h5>



		</div>



	</div>
    '''
    return data
