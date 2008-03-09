Summary:	Funky application dock for X11
Name:		kiba-dock
Version:	0.0.722
Release:	1
Group:		System/X11
URL:		http://kiba-dock.org/
Source0: %{name}-r722.tar.bz2
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

%files
%defattr(644,root,root,755)
%{_sysconfdir}/gconf/schemas/kiba.schemas
%{_bindir}/%{name} %{_bindir}/akamaru %{_bindir}/gset-kiba
%{_bindir}/kiba-icon-editor.py %{_bindir}/kiba-systray.py
%{_bindir}/populate-dock.sh
%py_puresitedir/SimpleGladeApp.py
%{_iconsdir}/hicolor/*/apps/kiba*.png
%{_bindir}/%{name} %{_bindir}/akamaru %{_bindir}/gset-kiba
%{_bindir}/kiba-icon-editor.py %{_bindir}/kiba-systray.py
%{_bindir}/populate-dock.sh %{_bindir}/%{name} %{_bindir}/akamaru
%{_bindir}/gset-kiba %{_bindir}/kiba-icon-editor.py
%{_bindir}/kiba-systray.py %{_bindir}/populate-dock.sh
%{_datadir}/kiba-dock/*
%attr(755,root,root) %{_libdir}/%{name}/*.so*
%{_libdir}/%{name}/*.la*
%{_bindir}/%{name} %{_bindir}/akamaru %{_bindir}/gset-kiba
%{_bindir}/kiba-icon-editor.py %{_bindir}/kiba-systray.py
%{_bindir}/populate-dock.sh %{_bindir}/%{name} %{_bindir}/akamaru
%{_bindir}/gset-kiba %{_bindir}/kiba-icon-editor.py
%{_bindir}/kiba-systray.py %{_bindir}/populate-dock.sh
%{_datadir}/kiba-dock/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/kiba-dock.pc %{_libdir}/%{name}/*.a


%prep
%setup -q -n %{name}

# Fix x86_64 issue
sed -i "s,%{_libdir},%_libdir,g" dock/kiba-dock.c

%build
# This is a CVS snapshot, so we need to generate makefiles.
sh autogen.sh -V

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post
%post_install_gconf_schemas %{name}

%preun
%preun_uninstall_gconf_schemas %{name}

%clean
rm -rf $RPM_BUILD_ROOT
