Summary:	Funky application dock for X11
Name:		kiba-dock
Version:	0.0.722
Release:	1
Group:		System/X11
URL:		http://kiba-dock.org/
Source0:	%{name}-r722.tar.bz2
# Source0-md5: c1c59e9dfe2c9aa631f01eb97f742d50
License:	GPL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Funky dock for X11

%package devel
Summary:	Development files for kiba-dock
Group:		Development/X11
Requires:	%{name} = %{version}

%description devel
Headers for kiba-dock.

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_datadir}/kiba-dock
/usr/share/pixmaps/kiba-dock.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/kiba-dock/
/usr/lib/pkgconfig/kiba-dock.pc

%prep
%setup -q -n %{name}

%build
# This is a CVS snapshot, so we need to generate makefiles.
sh autogen.sh -V

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%post
%post_install_gconf_schemas %{name}

%preun
%preun_uninstall_gconf_schemas %{name}

%clean
rm -rf $RPM_BUILD_ROOT
