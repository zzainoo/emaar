from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from .templates_ar import *
from .templates_en import *

def list_projects(request, pk):
    try:
        post = Project.objects.get(pk=pk)
        header = Header.objects.all().filter(is_default=True).first()
        footer = Footer.objects.all().filter(is_default=True).first()
        data = ""
        data += get_header(header.short_code, "/")
        data += f'''
        <div class="section-wrapper">
        <div class="section8 section-rounded">
            <div >
                <p class="title">{post.name}</p>
                <br>
                
            </div>
            <div >
                <div class="shape animate__animated animate__pulse">
                    <img src="{post.image.url}" class="section-image" >
                </div>
            </div>
        </div>
    
    
    
    </div>
    
    <div class="section">
        {post.desc}
    </div>
        
        '''
        ctx = {
            'site': Site.objects.get(id=post.site.id),
            'components': data,
        }
        data += get_footer(footer.short_code)
        return render(request, 'base.html', ctx)
    except:
        return HttpResponse("404 not found")


def list_posts(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        header = Header.objects.all().filter(is_default=True).first()
        footer = Footer.objects.all().filter(is_default=True).first()
        data = ""
        data += get_header(header.short_code, "/")
        data += f'''
        <div class="section-wrapper">
        <div class="section8 section-rounded">
            <div >
                <p class="title">{post.name}</p>
                <br>

            </div>
            <div >
                <div class="shape animate__animated animate__pulse">
                    <img src="{post.image.url}" class="section-image" >
                </div>
            </div>
        </div>



    </div>

    <div class="section">
        {post.desc}
    </div>

        '''
        ctx = {
            'site': Site.objects.get(id=post.site.id),
            'components': data,
        }
        data += get_footer(footer.short_code)
        return render(request, 'base.html', ctx)
    except:
        return HttpResponse("404 not found")


# request.META.get('HTTP_ACCEPT_LANGUAGE', "ar-iq").split(",")[0].split("-")[0]
def main(request: WSGIRequest, page="/"):
    try:
        lang = request.GET.get("lang", None)
        if lang:
            if request.session.get('lang', 'ar') == "ar":
                request.session['lang'] = "en"
            else:
                request.session['lang'] = "ar"

        subdomains = []
        for sub in Site.objects.all():
            subdomains.append(sub.subdomain)

        subdomain = request.META['HTTP_HOST'].split('.')[0]
        if subdomain in subdomains:
            site = Site.objects.get(subdomain=subdomain)
        else:
            site = Site.objects.all().filter(is_homepage=True).first()

        main_page = CustomPage.objects.filter(site=site).filter(is_home=True).first()
        if page != "/" and page != "favicon.ico":
            try:
                main_page = CustomPage.objects.filter(site=site).filter(link=page).first()
            except:
                pass
        else:
            main_page = CustomPage.objects.filter(site=site).filter(is_home=True).first()
        components = []
        data = ""
        for short in main_page.short_codes.split(","):
            if request.session['lang'] == 'en':
                try:
                    data = get_header_en(short, page)
                except:
                    pass

                try:
                    data = get_section_en(short)
                except:
                    pass

                try:
                    data = get_spacer_en(short)
                except:
                    pass

                try:
                    data = get_counter_en(short)
                except:
                    pass

                try:
                    data = get_masonry_en(short)
                except:
                    pass

                try:
                    data = get_blog_en(short)
                except:
                    pass

                try:
                    data = get_project_en(short)
                except:
                    pass

                try:
                    data = get_footer_en(short)
                except:
                    pass

                try:
                    data = get_contact_en(short)
                except:
                    pass
            else:
                try:
                    data = get_header(short, page)
                except:
                    pass

                try:
                    data = get_section(short)
                except:
                    pass

                try:
                    data = get_spacer(short)
                except:
                    pass

                try:
                    data = get_counter(short)
                except:
                    pass

                try:
                    data = get_masonry(short)
                except:
                    pass

                try:
                    data = get_blog(short)
                except:
                    pass

                try:
                    data = get_project(short)
                except:
                    pass

                try:
                    data = get_footer(short)
                except:
                    pass

                try:
                    data = get_contact(short)
                except:
                    pass

            components.append(data)

        if request.session.get('lang', 'ar') == "ar":
            template = "base.html"
        else:
            template = "base_en.html"

        ctx = {
            'site': site,
            'main_page': main_page,
            'components': ''.join(components),
        }
        return render(request, template, ctx)
    except:
        return HttpResponse("404 not found")
