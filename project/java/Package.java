package example;

/* metamodel_version: 1.12.0 */
/* version: 3.0.1 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Refers to any unit of content that can be associated with a distribution of software.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Package extends SoftwareArtifact {

  private URI downloadLocation;
  private URI homePage;
  private URI packageUrl;
  private String packageVersion;
  private String sourceInfo;


}