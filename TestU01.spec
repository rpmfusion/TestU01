Summary:        Utilities for the statistical testing of uniform random number generators
Name:           TestU01
Version:        1.2.3
Release:        5%{?dist}
License:        Custom (Non-Commercial Use Only)
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Group:          Development/Libraries
Source0:        http://www.iro.umontreal.ca/~simardr/testu01/%{name}.zip
URL:            http://www.iro.umontreal.ca/~simardr/testu01/tu01.html

Patch1:         TestU01-format-security.patch
BuildRequires:  glibc-common
%if 0%{?rhel}==5
BuildRequires:  tetex-latex
%else
BuildRequires:  texlive-latex
%endif

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
Group: Development/Libraries
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description devel
Headers and shared object symbolic links for the %{name}.

%prep
%setup -q
%patch1 -p1 -b .fix-format-security
# Convert to utf-8
for file in COPYING param/LCGGranger.par; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%build
%configure
make  %{?_smp_mflags} V=1


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"


rm -rf %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_bindir}/tcode

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README COPYING NEWS
%docdir %{_datadir}/%{name}/doc
%{_datadir}/%{name}/doc
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%docdir %{_datadir}/%{name}/examples
%{_datadir}/%{name}/examples
%docdir %{_datadir}/%{name}/param
%{_datadir}/%{name}/param


%changelog
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

