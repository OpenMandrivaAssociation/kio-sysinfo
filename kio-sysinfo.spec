# svn co svn://anonsvn.kde.org/home/kde/trunk/playground/base/kio_sysinfo/
%define oname  kio_sysinfo
%define svn    1230316

Name:		kio-sysinfo
Version:	1.8.3
Release:	0.%{svn}.2
Summary:	KIO Slave sysinfo:/
License:	LGPL
Group:		System/Libraries
URL:		http://websvn.kde.org/trunk/playground/base/kio_sysinfo/ 
Source0:	%{oname}-%{svn}.tar.xz
Source1:	cpu.png
Source2:	sysinfo.png
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(hwinfo)

%description
KIO Slave sysinfo:/. It shows various information about your pc, 
like cpu, ram. kernel version, exc. It also shows the removable 
devices and partition (total space/available space) and you can open,
mount and unmount it from this KIO slave.

%files
%{_kde_libdir}/kde4/*
%{_kde_appsdir}/sysinfo
%{_kde_datadir}/applications/kde4/kfmclient_sysinfo.desktop
%{_kde_datadir}/kde4/services/ksysinfopart.desktop
%{_kde_datadir}/kde4/services/sysinfo.protocol
%{_kde_datadir}/mime/packages/x-sysinfo.xml

#--------------------------------------------------------------------

%prep
%setup -qn %{oname}

%build
%cmake_kde4 -DSYSINFO_DISTRO:STRING=rosa
%make

%install
%makeinstall_std -C build

%changelog
* Wed May 04 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.8.3-0.1230316.1mdv2011.0
+ Revision: 665330
- removed unnecessary BR dbus-devel
- fixed install
- new snapshot 1230316
- rebuild for hwinfo

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.8.3-0.822583.8mdv2011.0
+ Revision: 606265
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.8.3-0.822583.7mdv2010.1
+ Revision: 523157
- rebuilt for 2010.1

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add obsolete for 2009.0 -> 2010.0 upgrade

* Thu Oct 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.8.3-0.822583.5mdv2010.0
+ Revision: 455921
- fix build part 2
- Start to fix build
- Rebuild
- Rebuild

* Fri Aug 22 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.8.3-0.822583.2mdv2009.0
+ Revision: 275005
- Use mandriva icons ( need to commit upstream )
- Fix URL

* Tue Jun 24 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.8.3-0.822583.1mdv2009.0
+ Revision: 228739
- New kde4 based version

* Sun Jun 08 2008 Funda Wang <fwang@mandriva.org> 1.8.2-10mdv2009.0
+ Revision: 216987
- rebuild for new major of hwinfo

* Thu May 08 2008 Helio Chissini de Castro <helio@mandriva.com> 1.8.2-9mdv2009.0
+ Revision: 204707
- Move to /opt

* Tue Apr 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.8.2-8mdv2008.1
+ Revision: 191468
- Use neutral icon again

* Wed Mar 26 2008 Helio Chissini de Castro <helio@mandriva.com> 1.8.2-7mdv2008.1
+ Revision: 190353
- Fix for bug https://qa.mandriva.com/show_bug.cgi?id=39173 - Proper dbus/hal device handling

* Thu Jan 03 2008 Oden Eriksson <oeriksson@mandriva.com> 1.8.2-6mdv2008.1
+ Revision: 141781
- rebuilt against openldap-2.4.7 libs

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Oct 21 2007 Funda Wang <fwang@mandriva.org> 1.8.2-5mdv2008.1
+ Revision: 100829
- Updated patch0 from bug#32822

* Fri Oct 12 2007 Funda Wang <fwang@mandriva.org> 1.8.2-4mdv2008.1
+ Revision: 97268
- Rename to kio-sysinfo as sysinfo is too confusing

* Thu Sep 27 2007 Funda Wang <fwang@mandriva.org> 1.8.2-3mdv2008.0
+ Revision: 93343
- really fix bug#32031

* Tue Aug 28 2007 Helio Chissini de Castro <helio@mandriva.com> 1.8.2-2mdv2008.0
+ Revision: 72846
- Fix mimelnk placement

* Tue Aug 21 2007 Funda Wang <fwang@mandriva.org> 1.8.2-1mdv2008.0
+ Revision: 68729
- New version 1.8.2

  + Eskild Hustvedt <eskild@mandriva.org>
    - Fixed description

* Sat Aug 04 2007 Funda Wang <fwang@mandriva.org> 1.8.1-1mdv2008.0
+ Revision: 58918
- Rediff uz patch

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - new version
    - bzip2 sources

* Wed Jul 25 2007 Funda Wang <fwang@mandriva.org> 1.8-2mdv2008.0
+ Revision: 55432
- Add uz translation to fix mdvbug#32031

* Tue Jul 24 2007 Funda Wang <fwang@mandriva.org> 1.8-1mdv2008.0
+ Revision: 55039
- New version
- uz translation has been merged upstream
- do not use autotools for kde packages
- use aclocal
- BR libhd
- Replace images with icons here: http://www.kde-look.org/content/show.php?content=61727
- New verison
- rediff patch

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New patch for Uzbek translations (thanks  to Mashrab Kuvatov)
    - [FEATURE] Add Uzbek translations ( thanks to Mashrab Kuvatov) (bug report #32031)

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 1.3-4mdv2008.0
+ Revision: 36204
- rebuild with correct optflags

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    -Patch0: Make Sysinfo:/ display Mandriva Linux on System: instead of nothing

* Mon Jun 04 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.3-2mdv2008.0
+ Revision: 35108
- Fix File List
- Import sysinfo

