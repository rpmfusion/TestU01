%global __brp_check_rpaths %{nil}
Summary:        Utilities for the statistical testing of uniform random number generators
Name:           TestU01
Version:        1.2.3
Release:        24%{?dist}
License:        Custom (Non-Commercial Use Only)
URL:            http://simul.iro.umontreal.ca/testu01/tu01.html
Source0:        http://simul.iro.umontreal.ca/testu01/%{name}.zip

Patch1:         TestU01-format-security.patch
Patch2:         upstream-fix-migration_to_C23-cleanup.patch.patch
BuildRequires:  gcc-c++
BuildRequires:  glibc-common
BuildRequires:  texlive-latex

%description 
TestU01 is a software library, implemented in the ANSI C language, and offering
a collection of utilities for the empirical statistical testing of uniform
random number generators.

The library implements several types of random number generators in generic
form, as well as many specific generators proposed in the literature or found
in widely-used software. It provides general implementations of the classical
statistical tests for random number generators, as well as several others
proposed in the literature, and some original ones. These tests can be applied
to the generators predefined in the library and to user-defined generators.
Specific tests suites for either sequences of uniform random numbers in [0,1]
or bit sequences are also available. Basic tools for plotting vectors of points
produced by generators are provided as well.

Additional software permits one to perform systematic studies of the
interaction between a specific test and the structure of the point sets
produced by a given family of random number generators. That is, for a given
kind of test and a given class of random number generators, to determine how
large should be the sample size of the test, as a function of the generator's
period length, before the generator starts to fail the test systematically.

%package devel
Summary: Headers and shared object symbolic links for the %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description devel
Headers and shared object symbolic links for the %{name}.

%prep
%setup -q
%patch -P1 -p1 -b .fix-format-security
%patch -P2 -p1 -b .fix-c23-issue
# Convert to utf-8
for file in COPYING param/LCGGranger.par; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%build
%configure
%make_build


%install
%make_install


rm -rf %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_bindir}/tcode

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README NEWS
%license  COPYING
%docdir %{_datadir}/%{name}/doc
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/doc
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%docdir %{_datadir}/%{name}/examples
%{_datadir}/%{name}/examples
%docdir %{_datadir}/%{name}/param
%{_datadir}/%{name}/param


%changelog
* Mon Feb 02 2026 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sun Jul 27 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jan 29 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.3-10
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 1.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 21 2016 Sérgio Basto <sergio@serjux.com> - 1.2.3-5
- Fix FTBFS (rfbz#3440)

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.2.3-3
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 25 2012 Jirka Hladky <hladky.jiri@gmail.com> - 1.2.3-2
 - Changed license to "Custom (Non-Commercial Use Only)"
* Tue Dec 20 2011 Jirka Hladky <hladky.jiri@gmail.com> - 1.2.3-1
 - Initial package version

