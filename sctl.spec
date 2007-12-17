%define name sctl 
%define version 0.2.3
%define release %mkrel 4

Name: %{name} 
Summary: A program designed to control Bearcat model BC-895xlt & BC-245xlt scanners
Version: %{version} 
Release: %{release} 
Source: http://www.obairlann.net/~reaper/sctl/tarfiles/%{name}-%{version}.tar.bz2 
URL: http://www.obairlann.net/~reaper/sctl/
Group: Communications 
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

