#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.2
%define		kframever	5.91.0
%define		qtver		5.15.2
%define		kaname		kpat
Summary:	kpat
Name:		ka5-%{kaname}
Version:	23.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	b77960e495b7f761fd7a2437a91a3fa7
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.20
BuildRequires:	freecell-solver-devel
BuildRequires:	gettext-tools
BuildRequires:	ka5-libkdegames-devel >= 22.03.80
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kguiaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	Qt5Core >= %{qtver}
Requires:	Qt5Svg >= %{qtver}
Requires:	Qt5Widgets >= %{qtver}
Requires:	hicolor-icon-theme
Requires:	ka5-libkdegames >= 22.03.80
Requires:	kf5-kcompletion >= %{kframever}
Requires:	kf5-kconfig >= %{kframever}
Requires:	kf5-kconfigwidgets >= %{kframever}
Requires:	kf5-kcoreaddons >= %{kframever}
Requires:	kf5-kcrash >= %{kframever}
Requires:	kf5-kdbusaddons >= %{kframever}
Requires:	kf5-kguiaddons >= %{kframever}
Requires:	kf5-ki18n >= %{kframever}
Requires:	kf5-kio >= %{kframever}
Requires:	kf5-knewstuff >= %{kframever}
Requires:	kf5-kwidgetsaddons >= %{kframever}
Requires:	kf5-kxmlgui >= %{kframever}
Requires:	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KPat (aka KPatience) is a relaxing card sorting game. To win the game
a player has to arrange a single deck of cards in certain order
amongst each other.

%description -l pl.UTF-8
KPat (znany również jako KPatience) jest odprężającą grą w układanie
kart. Aby wygrać grę, gracz musi ułożyć pojedynczą talię kart w
odpowiedniej kolejności względem siebie.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DWITH_BH_SOLVER:BOOL=OFF \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database
%update_icon_cache hicolor
%update_desktop_database

%postun
%update_mime_database
%update_icon_cache hicolor
%update_desktop_database

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpat
%attr(755,root,root) %{_libdir}/libkcardgame.so
%{_desktopdir}/org.kde.kpat.desktop
%{_datadir}/config.kcfg/kpat.kcfg
%{_iconsdir}/hicolor/*/apps/kpat.png
%{_datadir}/kpat
%{_datadir}/knsrcfiles/kcardtheme.knsrc
%{_datadir}/knsrcfiles/kpat.knsrc
%{_datadir}/metainfo/org.kde.kpat.appdata.xml
%{_datadir}/mime/packages/kpatience.xml
%{_datadir}/qlogging-categories5/kpat.categories
%{_mandir}/man6/kpat.6*
%lang(ca) %{_mandir}/ca/man6/kpat.6*
%lang(de) %{_mandir}/de/man6/kpat.6*
%lang(es) %{_mandir}/es/man6/kpat.6*
%lang(et) %{_mandir}/et/man6/kpat.6*
%lang(it) %{_mandir}/it/man6/kpat.6*
%lang(nl) %{_mandir}/nl/man6/kpat.6*
%lang(pt) %{_mandir}/pt/man6/kpat.6*
%lang(pt_BR) %{_mandir}/pt_BR/man6/kpat.6*
%lang(ru) %{_mandir}/ru/man6/kpat.6*
%lang(sv) %{_mandir}/sv/man6/kpat.6*
%lang(uk) %{_mandir}/uk/man6/kpat.6*
