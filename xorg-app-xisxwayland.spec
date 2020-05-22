Summary:	xisxwayland tool to check whether X server is Xwayland
Summary(pl.UTF-8):	Narzędzie xisxwayland do sprawdzania, czy serwer X to Xwayland
Name:		xorg-app-xisxwayland
Version:	1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xisxwayland-%{version}.tar.xz
# Source0-md5:	c4a140eb71ddd8aff9a5ac8e5d2404c4
URL:		https://xorg.freedesktop.org/
BuildRequires:	meson >= 0.41.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xisxwayland is a tool to be used within shell scripts to determine
whether the X server in use is Xwayland.

%description -l pl.UTF-8
xisxwayland to narzędzie, którego można używać w skryptach powłoki do
określenia, czy używany serwer X to Xwayland.

%prep
%setup -q -n xisxwayland-%{version}

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README.md
%attr(755,root,root) %{_bindir}/xisxwayland
%{_mandir}/man1/xisxwayland.1*
