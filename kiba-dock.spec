######		Unknown group!
Summary:	Funky application dock for X11
Name:		kiba-dock
Version:	0.0.731
Release:	1
Group:		System/X11
URL:		http://kiba-dock.org/
Source0:	%{name}-r731.tar.bz2
# Source0-md5:	7083cd4f998960bd3f22e2778e3029d8
License:	GPL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Funky dock for X11

%package devel
######		Unknown group!
Summary:	Development files for kiba-dock
Group:		Development/X11
Requires:	%{name} = %{version}

%description devel
Headers for kiba-dock.

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

install -d $RPM_BUILD_ROOT%{_libdir}/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%dir %{_libdir}/kiba-dock
%{_datadir}/kiba-dock
%{_pixmapsdir}/kiba-dock.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/kiba-dock/
%{_pkgconfigdir}/kiba-dock.pc
