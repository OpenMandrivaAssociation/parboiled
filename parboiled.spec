%{?_javapackages_macros:%_javapackages_macros}
Name:          parboiled
Version:       1.0.2
Release:       6.1%{?dist}
Summary:       Java/Scala library providing parsing of input text based on PEGs
License:       ASL 2.0
URL:           http://parboiled.org/
Source0:       https://github.com/sirthias/parboiled/archive/%{version}.tar.gz
# for build see https://github.com/sirthias/parboiled/wiki/Building-parboiled
Source1:       http://repo1.maven.org/maven2/org/%{name}/%{name}-core/%{version}/%{name}-core-%{version}.pom
Source2:       http://repo1.maven.org/maven2/org/%{name}/%{name}-java/%{version}/%{name}-java-%{version}.pom
# customized aggregator pom
Source3:       %{name}-%{version}-pom.xml

BuildRequires: java-devel

BuildRequires: mvn(asm:asm)
BuildRequires: mvn(asm:asm-analysis)
BuildRequires: mvn(asm:asm-tree)
BuildRequires: mvn(asm:asm-util)

%if 0
# TODO 
BuildRequires: mvn(org.scala-lang:scala-library)
# test deps
BuildRequires: mvn(org.scalatest:scalatest_2.10)
BuildRequires: mvn(org.testng:testng)

# use https://github.com/davidB/scala-maven-plugin
BuildRequires: scala-maven-plugin
BuildRequires: maven-surefire-provider-testng
%endif

BuildRequires: maven-local


BuildArch:     noarch

%description
parboiled is a mixed Java/Scala library providing for lightweight and
easy-to-use, yet powerful and elegant parsing of arbitrary input text
based on Parsing expression grammars (PEGs). PEGs are an alternative to
context free grammars (CFGs) for formally specifying syntax, they
make a good replacement for regular expressions and generally have quite
a few advantages over the "traditional" way of building parsers via CFGs.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

find . -name "*.class" -delete
find . -name "*.jar" -delete

cp -p %{SOURCE1} %{name}-core/pom.xml
cp -p %{SOURCE2} %{name}-java/pom.xml
#cp -p %%{SOURCE?} %%{name}-scala/pom.xml
cp -p %{SOURCE3} pom.xml

%mvn_file :%{name}-core %{name}/core
%mvn_file :%{name}-java %{name}/java

%build

# test skipped unavailable dep org.scalatest scalatest_2.9.0 1.6.1
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8
 
%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc CHANGELOG LICENSE README.markdown

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 gil cattaneo <puntogil@libero.it> 1.0.2-5
- switch to XMvn
- minor changes to adapt to current guideline

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.2-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Feb 05 2013 gil cattaneo <puntogil@libero.it> 1.0.2-3
- fix unowned directory rhbz#907517

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 gil cattaneo <puntogil@libero.it> 1.0.2-1
- initial rpm