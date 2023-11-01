Name:           gnome-logs
Version:        3.36.0
Release:        8%{?dist}
Summary:        Log viewer for the systemd journal

License:        GPLv3+
URL:            https://wiki.gnome.org/Apps/Logs
Source0:        https://download.gnome.org/sources/%{name}/3.36/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  itstool
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  /usr/bin/appstream-util
Requires:       gsettings-desktop-schemas

Patch10001: 0001-gl-application.c-add-four-shortcuts.patch
Patch10002: 0002-help-overlay.ui-Add-three-shortcuts.patch

Patch20001: 0001-gl-window-Set-default-width-height.patch

%description
A log viewer for the systemd journal.

%prep
%autosetup -S git


%build
%meson -Dman=true
%meson_build


%install
%meson_install
%find_lang %{name} --with-gnome


%check
%meson_test


%files -f %{name}.lang
%doc AUTHORS README NEWS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/org.gnome.Logs.desktop
%{_datadir}/dbus-1/services/org.gnome.Logs.service
%{_datadir}/glib-2.0/schemas/org.gnome.Logs.*.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Logs.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Logs-symbolic.svg
%{_datadir}/metainfo/org.gnome.Logs.appdata.xml
%{_mandir}/man1/gnome-logs.1*


%changelog
* Wed Jan 25 2023 Ray Strode <rstrode@redhat.com> - 3.36.0-8
- Fix window resizing
  Resolves: #2035832

* Wed Dec 14 2022 Ray Strode <rstrode@redhat.com> - 3.36.0-7
- Fix shortcuts
  Resolves: #2062860

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 3.36.0-6
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 3.36.0-5
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 2020 David King <amigadave@amigadave.com> - 3.36.0-1
- Update to 3.36.0 (#1834692)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 David King <amigadave@amigadave.com> - 3.34.0-1
- Update to 3.34.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 David King <amigadave@amigadave.com> - 3.33.2-1
- Update to 3.33.2

* Tue Apr 23 2019 David King <amigadave@amigadave.com> - 3.33.1-1
- Update to 3.33.1 (#1702129)

* Mon Apr 08 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 David King <amigadave@amigadave.com> - 3.31.4-1
- Update to 3.31.4

* Mon Dec 10 2018 David King <amigadave@amigadave.com> - 3.31.3-1
- Update to 3.31.3

* Mon Nov 12 2018 David King <amigadave@amigadave.com> - 3.31.2-1
- Update to 3.31.2

* Mon Sep 03 2018 David King <amigadave@amigadave.com> - 3.30.0-1
- Update to 3.30.0

* Tue Jul 17 2018 David King <amigadave@amigadave.com> - 3.29.4-1
- Update to 3.29.4 (#1601640)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.29.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 David King <amigadave@amigadave.com> - 3.29.1-1
- Update to 3.29.1 (#1568395)

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Tue Mar 06 2018 David King <amigadave@amigadave.com> - 3.27.92-1
- Update to 3.27.92

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 David King <amigadave@amigadave.com> - 3.27.90-1
- Update to 3.27.90

* Mon Jan 08 2018 David King <amigadave@amigadave.com> - 3.27.4-1
- Update to 3.27.4

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.27.3-2
- Remove obsolete scriptlets

* Mon Dec 11 2017 David King <amigadave@amigadave.com> - 3.27.3-1
- Update to 3.27.3

* Mon Nov 13 2017 David King <amigadave@amigadave.com> - 3.27.2-1
- Update to 3.27.2 (#1512514)

* Fri Oct 20 2017 David King <amigadave@amigadave.com> - 3.27.1-1
- Update to 3.27.1 (#1504344)

* Mon Sep 11 2017 David King <amigadave@amigadave.com> - 3.26.0-1
- Update to 3.26.0

* Mon Sep 04 2017 David King <amigadave@amigadave.com> - 3.25.92-1
- Update to 3.25.92

* Mon Aug 21 2017 David King <amigadave@amigadave.com> - 3.25.91-1
- Update to 3.25.91

* Tue Aug 08 2017 David King <amigadave@amigadave.com> - 3.25.90-1
- Update to 3.25.90

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 David King <amigadave@amigadave.com> - 3.25.4-1
- Update to 3.25.4

* Tue Apr 25 2017 David King <amigadave@amigadave.com> - 3.25.1-1
- Update to 3.25.1

* Mon Apr 10 2017 David King <amigadave@amigadave.com> - 3.24.1-1
- Update to 3.24.1

* Tue Mar 21 2017 David King <amigadave@amigadave.com> - 3.24.0-1
- Update to 3.24.0

* Tue Feb 28 2017 David King <amigadave@amigadave.com> - 3.23.91-1
- Update to 3.23.91 (#1427344)

* Tue Feb 14 2017 David King <amigadave@amigadave.com> - 3.23.90-1
- Update to 3.23.90 (#1421886)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 David King <amigadave@amigadave.com> - 3.23.4-1
- Update to 3.23.4

* Mon Dec 12 2016 David King <amigadave@amigadave.com> - 3.23.3-1
- Update to 3.23.3

* Tue Nov 22 2016 David King <amigadave@amigadave.com> - 3.23.2-1
- Update to 3.23.2

* Tue Oct 25 2016 David King <amigadave@amigadave.com> - 3.23.1-1
- Update to 3.23.1

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 3.22.1-2
- Don't set group tags
- Use make_install macro

* Mon Oct 10 2016 David King <amigadave@amigadave.com> - 3.22.1-1
- Update to 3.22.1

* Tue Sep 20 2016 David King <amigadave@amigadave.com> - 3.22.0-1
- Update to 3.22.0

* Tue Sep 13 2016 David King <amigadave@amigadave.com> - 3.21.92-1
- Update to 3.21.92

* Tue Aug 16 2016 David King <amigadave@amigadave.com> - 3.21.90-1
- Update to 3.21.90

* Tue Jun 21 2016 David King <amigadave@amigadave.com> - 3.21.3-1
- Update to 3.21.3

* Mon Apr 11 2016 David King <amigadave@amigadave.com> - 3.20.1-1
- Update to 3.20.1

* Tue Mar 22 2016 David King <amigadave@amigadave.com> - 3.20.0-1
- Update to 3.20.0

* Tue Mar 15 2016 David King <amigadave@amigadave.com> - 3.19.92-1
- Update to 3.19.92

* Mon Feb 29 2016 David King <amigadave@amigadave.com> - 3.19.91-1
- Update to 3.19.91

* Tue Feb 16 2016 David King <amigadave@amigadave.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 David King <amigadave@amigadave.com> - 3.19.4-1
- Update to 3.19.4

* Mon Dec 14 2015 David King <amigadave@amigadave.com> - 3.19.3-1
- Update to 3.19.3

* Tue Nov 24 2015 David King <amigadave@amigadave.com> - 3.19.2-1
- Update to 3.19.2

* Mon Oct 26 2015 David King <amigadave@amigadave.com> - 3.19.1-1
- Update to 3.19.1

* Tue Oct 13 2015 David King <amigadave@amigadave.com> - 3.18.1-1
- Update to 3.18.1

* Tue Sep 22 2015 David King <amigadave@amigadave.com> - 3.18.0-1
- Update to 3.18.0

* Tue Sep 01 2015 David King <amigadave@amigadave.com> - 3.17.91-1
- Update to 3.17.91

* Mon Aug 17 2015 David King <amigadave@amigadave.com> - 3.17.90-1
- Update to 3.17.90

* Tue Jul 21 2015 David King <amigadave@amigadave.com> - 3.17.4-1
- Update to 3.17.4

* Mon Jun 22 2015 David King <amigadave@amigadave.com> - 3.17.3-1
- Update to 3.17.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 David King <amigadave@amigadave.com> - 3.17.2-1
- Update to 3.17.2

* Mon Apr 27 2015 David King <amigadave@amigadave.com> - 3.17.1-1
- Update to 3.17.1

* Mon Apr 13 2015 David King <amigadave@amigadave.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 David King <amigadave@amigadave.com> - 3.16.0-1
- Update to 3.16.0

* Mon Mar 16 2015 David King <amigadave@amigadave.com> - 3.15.92-1
- Update to 3.15.92

* Mon Mar 02 2015 David King <amigadave@amigadave.com> - 3.15.91-1
- Update to 3.15.91

* Wed Feb 18 2015 David King <amigadave@amigadave.com> - 3.15.90-1
- Update to 3.15.90
- Use license macro for COPYING

* Mon Jan 19 2015 David King <amigadave@amigadave.com> - 3.15.4-1
- Update to 3.15.4

* Mon Dec 15 2014 David King <amigadave@amigadave.com> - 3.15.3-1
- Update to 3.15.3

* Mon Nov 24 2014 David King <amigadave@amigadave.com> - 3.15.2-1
- Update to 3.15.2

* Tue Oct 28 2014 David King <amigadave@amigadave.com> - 3.15.1-1
- Update to 3.15.1

* Wed Oct 15 2014 David King <amigadave@amigadave.com> - 3.14.1-2
- Add HighContrast application icon (#1152796)

* Mon Oct 13 2014 David King <amigadave@amigadave.com> - 3.14.1-1
- Update to 3.14.1

* Tue Sep 23 2014 David King <amigadave@amigadave.com> - 3.14.0-1
- Update to 3.14.0
- Do not own the appdata directory

* Mon Sep 15 2014 David King <amigadave@amigadave.com> - 3.13.92-1
- Update to 3.13.92

* Mon Sep 01 2014 David King <amigadave@amigadave.com> - 3.13.91-1
- Update to 3.13.91

* Mon Aug 18 2014 David King <amigadave@amigadave.com> - 3.13.90-1
- Update to 3.13.90

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 David King <amigadave@amigadave.com> - 3.13.4-1
- Update to 3.13.4

* Mon Jun 30 2014 David King <amigadave@amigadave.com> - 3.13.3-2
- Fix AppData reference to desktop file

* Mon Jun 23 2014 David King <amigadave@amigadave.com> - 3.13.3-1
- Update to 3.13.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 David King <amigadave@amigadave.com> - 3.13.2-1
- Update to 3.13.2

* Tue Apr 29 2014 David King <amigadave@amigadave.com> - 3.13.1-1
- Update to 3.13.1

* Mon Apr 14 2014 David King <amigadave@amigadave.com> - 3.12.1-1
- Update to 3.12.1

* Mon Mar 17 2014 David King <amigadave@amigadave.com> - 3.12.0-1
- Update to 3.12.0

* Mon Mar 17 2014 David King <amigadave@amigadave.com> - 3.11.92-1
- Update to 3.11.92

* Sat Mar 08 2014 David King <amigadave@amigadave.com> - 3.11.91-2
- Use pkgconfig with BuildRequires

* Mon Mar 03 2014 David King <amigadave@amigadave.com> - 3.11.91-1
- Update to 3.11.91

* Tue Feb 18 2014 David King <amigadave@amigadave.com> - 3.11.90-1
- Update to 3.11.90
- Validate the desktop file and AppData using "make check"

* Tue Feb 04 2014 David King <amigadave@amigadave.com> - 3.11.5-1
- Update to 3.11.5

* Tue Dec 17 2013 David King <amigadave@amigadave.com> - 3.11.3-1
- Update to 3.11.3

* Thu Dec 12 2013 David King <amigadave@amigadave.com> - 3.11.2-1
- New package.
