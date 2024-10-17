%define name sctl 
%define version 0.2.3
%define release 9

Name: %{name} 
Summary: A program designed to control Bearcat model BC-895xlt & BC-245xlt scanners
Version: %{version} 
Release: %{release} 
Source: http://www.obairlann.net/~reaper/sctl/tarfiles/%{name}-%{version}.tar.bz2 
URL: https://www.obairlann.net/~reaper/sctl/
Group: Communications 
BuildRoot: %{_tmppath}/%{name}-buildroot 
License: GPL

%description
Sctl is a program designed to control Bearcat model BC-895xlt scanners. It
may control other scanners with PC-control (aka, "serial") ports on them 
(no testing has been done yet). It provides a command-line interface, and 
is extremely small (it would be described as "fast" too, but 9600 baud 
communication makes anything seem slow). It should work with any *nix system, 
and more targets will be tested as time goes on. At present it's known to 
work with Debian 1.2 and Redhat 6.2, indicating a good chance it'll work 
on any reasonably modern Linux system.  Compatible scanners include the 
BC-245xlt.

%prep 
rm -rf $RPM_BUILD_ROOT 

%setup 

%build 

%make

%install
mkdir -p $RPM_BUILD_ROOT%_bindir

install sctl $RPM_BUILD_ROOT%_bindir

# cleanup
find . -type d -name CVS | xargs rm -rf

%clean 
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root,0755)
%_bindir/*
%doc BUGS Changelog CREDITS LICENSE NEWS README
%doc docs/*



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.2.3-8mdv2010.0
+ Revision: 433635
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.2.3-7mdv2009.0
+ Revision: 260584
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.2.3-6mdv2009.0
+ Revision: 252233
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.2.3-4mdv2008.1
+ Revision: 127104
- kill re-definition of %%buildroot on Pixel's request
- import sctl


* Thu Jan 05 2005 Lenny Cartier <lenny@mandriva.com> 0.2.3-4mdk
- rebuild

* Fri Jun 04 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.2.3-3mdk
- rebuild

* Sat Feb 01 2003 Lenny Cartier <lenny@mandrakesoft.com 0.2.3-2mdk
- rebuild

* Mon Nov 18 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.2.3-1mdk
- 0.2.3
- remove CVS entries
- from Roger <roger@linuxfreemail.com> 
