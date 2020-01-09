%global _changelog_trimtime %(date +%s -d "1 year ago")

%define _default_patch_fuzz 2
%{!?python_sitelib: %define python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary:   Compat package with PackageKit 0.8.9 libraries
Name:      compat-PackageKit08
Version:   0.8.9
Release:   1%{?dist}
License:   GPLv2+ and LGPLv2+
URL:       http://www.packagekit.org
Source0:   http://www.packagekit.org/releases/PackageKit-%{version}.tar.xz

# Upstream already
Patch5: 0001-Do-not-install-into-python_sitelib.patch

# required by patch4
BuildRequires: automake gtk-doc libtool
BuildRequires: glib2-devel >= 2.16.1
BuildRequires: dbus-devel  >= 1.1.1
BuildRequires: dbus-glib-devel >= 0.74
BuildRequires: pam-devel
BuildRequires: libX11-devel
BuildRequires: xmlto
BuildRequires: gtk-doc
BuildRequires: gcc-c++
BuildRequires: sqlite-devel
BuildRequires: NetworkManager-devel
BuildRequires: polkit-devel >= 0.92
BuildRequires: libtool
BuildRequires: gtk2-devel
BuildRequires: gtk3-devel
BuildRequires: docbook-utils
BuildRequires: gnome-doc-utils
BuildRequires: python-devel
BuildRequires: perl(XML::Parser)
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: libgudev1-devel
BuildRequires: libarchive-devel
BuildRequires: pango-devel
BuildRequires: fontconfig-devel
BuildRequires: systemd-devel
BuildRequires: gobject-introspection-devel

%description
Compatibility package with PackageKit 0.8 libraries.

%package -n compat-libpackagekit-glib2-16
Summary: Compatibility package with PackageKit 0.8 libraries
Conflicts: PackageKit-glib < 0.9

%description -n compat-libpackagekit-glib2-16
Compatibility package with PackageKit 0.8 libraries.

%prep
%setup -q -n PackageKit-%{version}
%patch5 -p1 -b .python_sitelib

NOCONFIGURE=1 ./autogen.sh

%build
%configure \
        --disable-static \
        --disable-yum \
        --disable-bash-completion \
        --with-default-backend=auto \
        --with-python-package-dir=%{python_sitearch} \
        --disable-local \
        --disable-strict \
        --disable-silent-rules \
        --disable-tests

make %{?_smp_mflags} V=1

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_sysconfdir}
rm -rf $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_prefix}/lib/systemd
rm -rf $RPM_BUILD_ROOT%{_prefix}/lib/udev
rm -rf $RPM_BUILD_ROOT%{_libdir}/girepository-1.0/
rm -rf $RPM_BUILD_ROOT%{_libdir}/gnome-settings-daemon-3.0/
rm -rf $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/
rm -rf $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/
rm -rf $RPM_BUILD_ROOT%{_libdir}/libpackagekit-glib2.la
rm -rf $RPM_BUILD_ROOT%{_libdir}/libpackagekit-glib2.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/mozilla/
rm -rf $RPM_BUILD_ROOT%{_libdir}/packagekit-backend/
rm -rf $RPM_BUILD_ROOT%{_libdir}/packagekit-plugins/
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
rm -rf $RPM_BUILD_ROOT%{_libdir}/pm-utils/
rm -rf $RPM_BUILD_ROOT%{_libdir}/pm-utils/
rm -rf $RPM_BUILD_ROOT%{python_sitearch}
rm -rf $RPM_BUILD_ROOT%{_libexecdir}
rm -rf $RPM_BUILD_ROOT%{_sbindir}
rm -rf $RPM_BUILD_ROOT%{_datadir}
rm -rf $RPM_BUILD_ROOT%{_localstatedir}

%post -n compat-libpackagekit-glib2-16 -p /sbin/ldconfig

%postun -n compat-libpackagekit-glib2-16 -p /sbin/ldconfig

%files -n compat-libpackagekit-glib2-16
%doc COPYING
%{_libdir}/libpackagekit-glib2.so.*

%changelog
* Tue May 05 2015 Richard Hughes <rhughes@redhat.com> - 0.8.9-1
- New compat package for RHEL
- Resolves: #1184214
